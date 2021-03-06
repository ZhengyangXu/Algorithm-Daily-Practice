#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (42.94%)
# Likes:    1862
# Dislikes: 0
# Total Accepted:    413.9K
# Total Submissions: 961.9K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(","}":"{","]":"["}
        for i in range(len(s)):
            if s[i] in dic.values():
                stack.append(s[i])
            elif s[i] in dic.keys():
                top = stack.pop() if stack else "*"
                if dic[s[i]] == top:
                    continue  
                else:
                    return False    
        return not stack   
   
                    
# @lc code=end

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {')':'(',']':'[','}':'{'}
#         for char in s:
#             if char in mapping:
#                 top_element = stack.pop() if stack else '#'
#                 if mapping[char] != top_element:
#                     return False 
#             else:
#                 stack.append(char)
#         return not stack
            