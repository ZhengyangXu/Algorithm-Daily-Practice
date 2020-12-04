#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (33.99%)
# Likes:    1047
# Dislikes: 0
# Total Accepted:    109.3K
# Total Submissions: 321.6K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left,right = 0,0  
        ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1 
            else:
                right += 1 
                
            if left == right:
                ans = max(ans,left+right)
            
            if right > left:
                left = right = 0 
        left = right = 0 
        for i in range(len(s)-1,-1,-1):
            if s[i] == "(":
                left += 1 
            else:
                right += 1 
            if left == right:
                ans = max(ans,left+right)
            if right < left:
                left = right = 0  
        return ans 
 
                 
 
# @lc code=end

    # def longestValidParentheses(self, s: str) -> int: ##DP
    #     if not s:
    #         return 0 
    #     dp = [0]*len(s)
    #     ans = 0
    #     for i in range(1,len(s)):
    #         if s[i] == ")":
    #             if s[i-1] == "(":
    #                 dp[i] = dp[i-2] + 2 if i - 2 >= 0 else 2 
    #             else:
    #                 if i -dp[i-1] > 0 and  s[i - dp[i-1] - 1] == "(":
    #                     dp[i] = dp [i-1] + dp[i-dp[i-1]-2] + 2 if i - dp[i-1] - 2 >= 0 else dp[i-1] + 2 
    #             ans = max(ans,dp[i])
    #     return max(dp)
    
    
    # def longestValidParentheses(self, s: str) -> int: ## 栈
    #     if not s:
    #         return 0
    #     stack = [-1]
    #     ans = 0
    #     for i in range(len(s)):
    #         if s[i] == "(":
    #             stack.append(i)
    #         else:
    #             stack.pop() 
    #             if not stack:
    #                 stack.append(i)
    #             else:
    #                 ans = max(ans,i-stack[-1])
                    
    #     return ans