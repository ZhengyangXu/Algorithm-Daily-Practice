#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (30.90%)
# Likes:    842
# Dislikes: 0
# Total Accepted:    85.8K
# Total Submissions: 258.9K
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
                m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0]*n]*m
        if obstacleGrid[0][0] == 1:
            return 0 
        else:
            dp[0][0] = 1 
            
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                break   
            dp[i][0] = 1  
        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                break 
            dp[0][j] == 1
            
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] == 0 
                else:
                    dp[i][j] == dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
# @lc code=end

