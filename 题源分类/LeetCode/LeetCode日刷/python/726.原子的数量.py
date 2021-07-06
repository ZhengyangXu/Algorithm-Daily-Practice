#
# @lc app=leetcode.cn id=726 lang=python3
#
# [726] 原子的数量
#
# https://leetcode-cn.com/problems/number-of-atoms/description/
#
# algorithms
# Hard (46.04%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    13.4K
# Total Submissions: 25.1K
# Testcase Example:  '"H2O"'
#
# 给定一个化学式formula（作为字符串），返回每种原子的数量。
#
# 原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
#
# 如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2
# 这个表达是不可行的。
#
# 两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。
#
# 一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
#
# 给定一个化学式 formula ，返回所有原子的数量。格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于
# 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
#
#
#
# 示例 1：
#
#
# 输入：formula = "H2O"
# 输出："H2O"
# 解释：
# 原子的数量是 {'H': 2, 'O': 1}。
#
#
# 示例 2：
#
#
# 输入：formula = "Mg(OH)2"
# 输出："H2MgO2"
# 解释：
# 原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
#
#
# 示例 3：
#
#
# 输入：formula = "K4(ON(SO3)2)2"
# 输出："K4N2O14S4"
# 解释：
# 原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
#
#
# 示例 4：
#
#
# 输入：formula = "Be32"
# 输出："Be32"
#
#
#
#
# 提示：
#
#
# 1
# formula 由小写英文字母、数字 '(' 和 ')' 组成。
# formula 是有效的化学式。
#
#
#


# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        map = defaultdict(lambda: 1)
        d = deque([])
        i = idx = 0
        while i < n:
            c = formula[i]
            if c == '(' or c == ')':
                d.append(c)
                i += 1
            else:
                if str.isdigit(c):
                    # 获取完整的数字，并解析出对应的数值
                    j = i
                    while j < n and str.isdigit(formula[j]):
                        j += 1
                    cnt = int(formula[i:j])
                    i = j
                    # 如果栈顶元素是 )，说明当前数值可以应用给「连续一段」的原子中
                    if d and d[-1] == ')':
                        tmp = []
                        d.pop()
                        while d and d[-1] != '(':
                            cur = d.pop()
                            map[cur] *= cnt
                            tmp.append(cur)
                        d.pop()

                        for k in range(len(tmp) - 1, -1, -1):
                            d.append(tmp[k])
                    # 如果栈顶元素不是 )，说明当前数值只能应用给栈顶的原子
                    else:
                        cur = d.pop()
                        map[cur] *= cnt
                        d.append(cur)
                else:
                    # 获取完整的原子名
                    j = i + 1
                    while j < n and str.islower(formula[j]):
                        j += 1
                    cur = formula[i:j] + "_" + str(idx)
                    idx += 1
                    map[cur] = 1
                    i = j
                    d.append(cur)

        #  将不同编号的相同原子进行合并
        mm = defaultdict(int)
        for key, cnt in map.items():
            atom = key.split("_")[0]
            mm[atom] += cnt

        # 对mm中的key进行排序作为答案
        ans = []
        for key in sorted(mm.keys()):
            if mm[key] > 1:
                ans.append(key+str(mm[key]))
            else:
                ans.append(key)
        return "".join(ans)

        
        



# @lc code=end
# 执行用时：36 ms, 在所有 Python3 提交中击败了90.12%的用户
# 内存消耗：15.2 MB, 在所有 Python3 提交中击败了8.72%的用户
import re


class Solution:
    pt = re.compile(
        "([A-Z][a-z]*)|([()])|(\d+)")  # 用正则表达式将 formula 分为元素、左右括号和数字分为三类

    def countOfAtoms(self, formula: str) -> str:
        formula = tuple(filter(bool, re.split(
            self.pt, formula)))  # 将 formula 按元素、左右括号和数字之间分隔为字符串数组
        # print(formula)
        total = defaultdict(int)  # 统计所有原子个数的字典
        stack = [
            1,
        ]  # 用来递归括号的栈，先把整个式子当成是在一个括号内。其元素为"重复倍数"。
        num = 1  # 局部（当前括号内的）个数，因为不写个数就是1个，故初值为1。
        for a in formula[::-1]:
            if a.isdigit():  # a是数字：当左边是元素则num为局部原子个数；当左边是括号则num为该括号对的重复倍数。
                num = int(a)
            else:
                mul = stack[-1]  # 取当前（括号内）的：重复倍数、统计字典。
                if a.isalpha():  # a是元素符号：要加上 重复倍数×局部原子个数 个。
                    total[a] += mul * num
                elif ')' == a:  # 是右括号（注意是逆序遍历）入栈。则num是新括号内的重复倍数，则要和总的重复倍数相乘。
                    stack.append(mul * num)
                elif '(' == a:  # 是左括号，将此对括号内的统计结果汇总到括号外。然后出栈。
                    stack.pop()  # cur_dict已经引用了，故pop不会导致统计结果丢失。
                num = 1  # ★易错！局部个数用了一次之后就要重置为1，如果是括号的重复倍数，则已经入栈记录了。
        return ''.join(
            key +
            (str(val) if val > 1 else '')  # 注意原子个数为1，则省略为''。最后用''作为分隔符连接所有字符串
            for key, val in sorted(total.items()))  # 要以元素字典序升序排序。

    def countOfAtoms(self, formula: str) -> str:
        ans = ""
        stack = [{}]
        n = len(formula)
        i = 0
        # 输入：formula = "K4(ON(SO3)2)2"
        # 输出："K4N2O14S4"
        while i < n:
            if formula[i].isupper():
                start = i
                while i < n - 1 and formula[i + 1].islower():
                    i += 1
                end = i
                atom = formula[start:end + 1]
                while i < n - 1 and formula[i + 1].isdigit():
                    i += 1
                print(f'大写字母,num:{formula[end+1:i+1]}')
                num = formula[end + 1:i + 1]

                stack[-1][atom] = int(num) if num else 1
                i += 1
                print(f'大写字母,i:{i},stack:{stack}')
            elif formula[i] == "(":
                stack.append({})
                i += 1
                print(stack)
            else:
                inner = stack.pop()
                print(f'inner:{inner}')
                start = i + 1
                while i < n - 1 and formula[i + 1].isdigit():
                    i += 1
                end = i
                num = int(formula[start:end + 1])
                print(f"),num:{num}")
                for key in inner:
                    inner[key] *= num
                    if key in stack[-1]:
                        stack[-1][key] += inner[key]
                    else:
                        stack[-1][key] = inner[key]
                print(f'stack[-1]:{stack[-1]},inner:{inner}')

                i += 1
                print(f'),i:{i},stack:{stack}')

        res = []
        for key, value in stack[0].items():
            res.append((key, value))
        res = sorted(res, key=lambda x: x[0])

        ans = "".join([x[0] + str(x[1]) if x[1] > 1 else x[0] for x in res])

        return ans

    def countOfAtoms(self, formula: str) -> str:
        # 倒着的时候， 记录map，乘的基数，迭代中的乘数，个数，个数的10进制位数，元素
        cnts, multiply, muls, num, num_count, atom = defaultdict(
            int), 1, [], 0, 0, ""
        for c in formula[::-1]:
            if c == ')':
                # 如果当前有统计的数字，乘的基数要叠加
                if num:
                    multiply *= num
                    muls.append(num)
                    num = num_count = 0
                else:
                    muls.append(1)
            elif c == '(':
                # 去除掉上一个乘数
                multiply //= muls.pop()
            elif str.isdigit(c):
                num += int(c) * (10**num_count)
                num_count += 1
            elif str.islower(c):
                atom += c
            else:
                atom += c
                # 注意我们在更新元素个数时，始终要考虑乘的基数
                if num:
                    cnts[atom[::-1]] += num * multiply
                else:
                    cnts[atom[::-1]] += multiply
                atom = ""
                num = num_count = 0
        return "".join(key if cnts[key] == 1 else key + str(cnts[key])
                       for key in sorted(cnts.keys()))
