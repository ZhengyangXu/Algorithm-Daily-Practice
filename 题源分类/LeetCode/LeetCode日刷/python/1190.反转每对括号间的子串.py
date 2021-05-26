#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#
# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
#
# algorithms
# Medium (58.98%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    27.8K
# Total Submissions: 43.5K
# Testcase Example:  '"(abcd)"'
#
# 给出一个字符串 s（仅含有小写英文字母和括号）。
#
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
#
# 注意，您的结果中 不应 包含任何括号。
#
#
#
# 示例 1：
#
# 输入：s = "(abcd)"
# 输出："dcba"
#
#
# 示例 2：
#
# 输入：s = "(u(love)i)"
# 输出："iloveu"
#
#
# 示例 3：
#
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
#
#
# 示例 4：
#
# 输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 2000
# s 中只有小写英文字母和括号
# 我们确保所有括号都是成对出现的
#
#
#


# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        if not s:
            return
        stack = []
        temp = []
        for c in s:
            if c == '(':
                if temp:
                    stack.append(temp)
                temp = []
            elif c.isalnum():
                temp.append(c)
            else:
                temp = temp[::-1]
                stack += temp 
                
                


# @lc code=end

# def reverseParentheses(self, s: str) -> str:
#     if not s:
#         return
#     res = []

#     for c in s:
#         if c != ')':
#             res.append(c)
#         else:
#             temp = []
#             while res and res[-1] != '(':
#                 temp.append(res.pop())
#             if res:
#                 res.pop()
#             res += temp
#     return ''.join(res)
    # def reverseParentheses(self, s: str) -> str:
    #     stack = []
    #     n = len(s)
    #     pair = [0] * n

    #     for i in range(n):
    #         if s[i] == '(':
    #             stack.append(i)
    #         if s[i] == ')':
    #             j = stack.pop()
    #             pair[i] = j
    #             pair[j] = i

    #     index = 0
    #     step = 1
    #     res = []
    #     while index < n:
    #         if s[index] == '(' or s[index] == ')':
    #             index = pair[index]
    #             step = -step
    #         else:
    #             res.append(s[index])
    #         index += step
    #     return ''.join(res)