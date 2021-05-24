#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#
# https://leetcode-cn.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (60.32%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    51.3K
# Total Submissions: 85K
# Testcase Example:  '"abcde"\n"ace"'
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
# 
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde"
# 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
# 
# 若这两个字符串没有公共子序列，则返回 0。
# 
# 
# 
# 示例 1:
# 
# 输入：text1 = "abcde", text2 = "ace" 
# 输出：3  
# 解释：最长公共子序列是 "ace"，它的长度为 3。
# 
# 
# 示例 2:
# 
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。
# 
# 
# 示例 3:
# 
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0。
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# 输入的字符串只含有小写英文字符。
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: ## 递归消除重复子问题
        m,n = len(text1),len(text2)
        memo = [[-1]*(n+1) for _ in range(m+1)]
        
        def dp(i,j):
            
            if i == m or j == n:
                return 0 
            if memo[i][j] != -1:
                return memo[i][j]
            
            if text1[i] == text2[j]:
                memo[i][j] = 1 + dp(i+1,j+1)
                
            else:
                memo[i][j] = max(dp(i+1,j),dp(i,j+1))
                
            return memo[i][j]
        return dp(0,0)        
                
## 思路：递归,i,j表示s1[0:i]和s2[0:j]最长的公共子串，两个字符串从后向前遍历                
        
# @lc code=end



    # def longestCommonSubsequence(self, text1: str, text2: str) -> int: ## 动态规划
    #     m,n = len(text1),len(text2)
        
    #     dp = [[0] * (n + 1) for _ in range(m + 1)] 
    #     #dp = [[0]*(n+1)]*(m+1)
        
    #     for i in range(1,m+1):
    #         for j in range(1,n+1):
    #             if text1[i-1] == text2[j-1]:
    #                 dp[i][j] = 1 + dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
    #     return dp[-1][-1]
                

## 思路：动态规划，自底向上。从最小的子问题开始，dp[i][j]表示s1[0:i]、s2[0:j]的最长公共子列，然后状态转移
## 如果s1[i] == s2[j],那么就是前一个状态+1的最长长度，如果两个不相等，则是dp[i-1][j]或dp[i][j-1]或dp[i-1][j-1],
## 但是dp[i-1][j-1]肯定是最小的，所以不用考虑也可.但是 dp = [[0] * (n + 1) for _ in range(m + 1)] 




    # def longestCommonSubsequence(self, text1: str, text2: str) -> int: ## 递归没有消除重复子问题 超过时间
    #     m,n = len(text1),len(text2)
        
    #     def dp(i,j):
            
    #         if i == -1 or j == -1:
    #             return 0   
            
    #         if text1[i] == text2[j]:
    #             ans = 1 + dp(i-1,j-1)
                
    #         else:
    #             ans = max(dp(i-1,j),dp(i,j-1))
            
    #         return ans  
    #     return dp(m-1,n-1)
    
    
    
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int: ## 递归消除重复子问题
    #     m,n = len(text1),len(text2)
    #     memo = [[-1] * (n) for _ in range(m)] 
    #     def dp(i,j):
            
    #         if i == -1 or j == -1:
    #             return 0   
    #         if memo[i][j] != -1:
    #             return memo[i][j]
    #         if text1[i] == text2[j]:
    #             memo[i][j] = 1 + dp(i-1,j-1)
                
    #         else:
    #             memo[i][j] = max(dp(i-1,j),dp(i,j-1))
            
    #         return memo[i][j]
    #     return dp(m-1,n-1)
        
                
## 思路：递归,i,j表示s1[0:i]和s2[0:j]最长的公共子串，两个字符串从后向前遍历          