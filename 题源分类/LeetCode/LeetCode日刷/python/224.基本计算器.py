#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode-cn.com/problems/basic-calculator/description/
#
# algorithms
# Hard (39.01%)
# Likes:    451
# Dislikes: 0
# Total Accepted:    42K
# Total Submissions: 103K
# Testcase Example:  '"1 + 1"'
#
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "1 + 1"
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：s = " 2-1 + 2 "
# 输出：3
# 
# 
# 示例 3：
# 
# 
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# 
# 
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        sign = 1 
        res = 0 
        
        i = 0 
        
        while i < len(s):
            if s[i] == " ":
                i += 1
            elif s[i] == "(":
                stack.append(sign)
                i += 1 
                
            elif s[i] == "+":
                sign = stack[-1]
                i += 1 
            elif s[i] == "-":
                sign = -stack[-1]
                i += 1 
            
            elif s[i] == ")":
                stack.pop()
                i += 1
                
            else:
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = 10 * num +  ord(s[i]) - ord('0') 
                    i += 1 
                    
                res += sign * num
                
        return res 
        
        
        
        
# @lc code=end

