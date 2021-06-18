#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
# https://leetcode-cn.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (20.80%)
# Likes:    807
# Dislikes: 0
# Total Accepted:    198.8K
# Total Submissions: 951.6K
# Testcase Example:  '"42"'
#
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
#
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：
#
#
# 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
# 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
# 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
#
#
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
#
# 在任何情况下，若函数不能进行有效的转换时，请返回 0 。
#
# 提示：
#
#
# 本题中的空白字符只包括空格字符 ' ' 。
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。如果数值超过这个范围，请返回  INT_MAX
# (2^31 − 1) 或 INT_MIN (−2^31) 。
#
#
#
#
# 示例 1:
#
# 输入: "42"
# 输出: 42
#
#
# 示例 2:
#
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
# 我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
#
#
# 示例 3:
#
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
#
#
# 示例 4:
#
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
# ⁠    因此无法执行有效的转换。
#
# 示例 5:
#
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
# 因此返回 INT_MIN (−2^31) 。
#
#
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        cur = 1 
        state = [{},
                 {"blank":1,"digit":3,"sign":2,"other":4},
                 {"digit":3,"blank":4,"sign":4,"other":4},
                 {"digit":3,"blank":4,"sign":4,"other":4},
                 {"blank":4,"digit":4,"sign":4,"other":4}]
        
        ans = ''
        sign = 1 
        def toChar(c):
            if c == " ":
                return "blank"
            if c in "+-": 
                return "sign"
            if c.isdigit():
                return "digit"
            return "other"
        
        for c in str:
            char = toChar(c)
            if char not in state[cur]:
                return ans 
            if not ans and char == "sign" and c=="-":
                sign = -1 
            if cur != 4:
                if char == "digit":
                    ans += c 
            else:
                break 
            cur = state[cur][char]    
                
        if len(ans) > 0 and int(ans) > 0x7fffffff:
            if sign == -1:
                return sign * 0x7fffffff - 1
            else:
                return 0x7fffffff
        return sign*int(ans) if ans else 0 
        
            

# @lc code=end

    def myAtoi(self, str: str) -> int:
        s = str.lstrip()
        if len(s) == 0:
            return 0
        sign = -1 if s[0] == '-' else 1
        if not (s[0].isdigit() or s[0] == '-' or s[0] == '+'):
            return 0
        ans = ''
        for i in range(0, len(s)):
            if i == 0 and (s[i] == '+' or s[i] == '-'):
                pass
            if s[i].isdigit():
                ans += s[i]
            if i + 2 > len(s) or not s[i + 1].isdigit():
                break
        ans = int(ans) if len(ans) > 0 else 0
        if ans > 0x7fffffff:
            if sign == -1:
                return sign * 0x7fffffff - 1
            else:
                return sign * 0x7fffffff
        return sign * ans

 def myAtoi(self, str: str) -> int:
        res,i,sign,length=0,0,1,len(str)
        maxint = 2**31 - 1 
        minint = -2 ** 31 
        bound = 2 ** 31 // 10 
        if not str:
            return 0 
        while str[i] == " ":
            i += 1 
            if i == length:
                return 0 
        if str[i] == "-":
            sign = -1 
        if str[i] in '+-':
            i += 1 
        for c in str[i:]:
            if not '0' <= c <= '9':
                break 
            if res > bound or res == bound and c >'7':
                return maxint if sign == 1 else minint 
            res = 10 * res + ord(c) - ord('0')
        return sign * res 
    def myAtoi(self, str: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+',str.lstrip())),2**31-1),-2**31)