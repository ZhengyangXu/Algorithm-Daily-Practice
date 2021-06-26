# /*
#  * @Author: Zhengyang Xu
#  * @Date: 2021-06-25 17:31:01
#  * @Last Modified by:   Zhengyang Xu
#  * @Last Modified time: 2021-06-25 17:31:01
#  */
#
# @lc app=leetcode.cn id=752 lang=python3
#

# [752] 打开转盘锁
#
# https://leetcode-cn.com/problems/open-the-lock/description/
#
# algorithms
# Medium (49.11%)
# Likes:    187
# Dislikes: 0
# Total Accepted:    26.3K
# Total Submissions: 53.6K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
# '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
#
#
#
# 示例 1:
#
#
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
#
#
# 示例 2:
#
#
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：
# 把最后一位反向旋转一次即可 "0000" -> "0009"。
#
#
# 示例 3:
#
#
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# 输出：-1
# 解释：
# 无法旋转到目标数字且不被锁定。
#
#
# 示例 4:
#
#
# 输入: deadends = ["0000"], target = "8888"
# 输出：-1
#
#
#
#
# 提示：
#
#
# 死亡列表 deadends 的长度范围为 [1, 500]。
# 目标数字 target 不会在 deadends 之中。
# 每个 deadends 和 target 中的字符串的数字会在 10,000 个可能的情况 '0000' 到 '9999' 中产生。
#
#
#


# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000' 
        if start == target:
            return 0 #
        if start in deadends:
            return -1 
        
        def update(s,visited):
            nxt = []
            for i,c in enumerate(s):
                nxt.append(s[:i]+str((int(c) + 1)%10) + s[i+1:])
                nxt.append(s[:i]+str((int(c)-1)%10) + s[i+1:]) 
            return nxt 
        
        front = set(start)
        back = set(target)
        visited = set()
        step = 0 
        while front and back:
            nxt_level = set()
            if len(front) > len(back):
                front,back = back,front
            for cur in front:
                if cur in deadends:
                    continue 
                if cur in back:
                    return step 
                nxts = update(cur)
                for nxt in nxts:
                    if nxt not in visited:
                        nxt_level.add(nxt)
                        visited.add(nxt)
            front = nxt_level
            step += 1 
        return -1 

# @lc code=end
## 思路：bug找了一个小时。。step的位置错了，visited的条件用错了。。一开始把visited加入了ends里，
## 这样新的节点一遇到deadends就continue。。无法进入第二轮循环。其次step放在了循环里，导致算成了
## 每个节点循环的次数。

    def openLock(self, deadends: List[str], target: str) -> int:
        def plus(s, i):
            s = list(s)
            if s[i] == "9":
                s[i] = "0"
            else:
                s[i] = str(int(s[i]) + 1)
            return ''.join(s)

        def minus(s, i):
            s = list(s)
            if s[i] == "0":
                s[i] = "9"
            else:
                s[i] = str(int(s[i]) - 1)
            return ''.join(s)

        step = 0
        stack = ["0000"]
        deadends = set(deadends)
        visited = set('0000')

        while stack:
            size = len(stack)

            for i in range(size):

                cur = stack.pop(0)

                if cur in deadends:
                    continue

                if cur == target:
                    return step

                for i in range(4):
                    ## up
                    up = plus(cur, i)
                    if up not in visited:
                        visited.add(up)
                        stack.append(up)

                    down = minus(cur, i)
                    if down not in visited:
                        visited.add(down)
                        stack.append(down)

            step += 1

        return -1

    def openLock(self, deadends: List[str], target: str) -> int:
        def plus(s, i):
            s = list(s)
            if s[i] == "9":
                s[i] = "0"
            else:
                s[i] = str(int(s[i]) + 1)
            return ''.join(s)

        def minus(s, i):
            s = list(s)
            if s[i] == "0":
                s[i] = "9"
            else:
                s[i] = str(int(s[i]) - 1)
            return ''.join(s)

        step = 0
        q1 = ["0000"]
        q2 = [target]
        deadends = set(deadends)
        visited = set('0000')

        while q1 and q2:
            temp = set()

            for cur in q1:
                if cur in deadends:
                    continue
                if cur in q2:
                    return step

                visited.add(cur)

                for i in range(4):
                    up = plus(cur, i)
                    if up not in visited:
                        temp.add(up)
                    down = minus(cur, i)
                    if down not in visited:
                        temp.add(down)

            step += 1
            q1 = q2
            q2 = temp

        return -1
