#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] 两个字符串的最小ASCII删除和
#
# https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (64.78%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    6.5K
# Total Submissions: 10.1K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。
# 
# 示例 1:
# 
# 
# 输入: s1 = "sea", s2 = "eat"
# 输出: 231
# 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
# 在 "eat" 中删除 "t" 并将 116 加入总和。
# 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
# 
# 
# 示例 2:
# 
# 
# 输入: s1 = "delete", s2 = "leet"
# 输出: 403
# 解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
# 将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
# 结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
# 如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
# 
# 
# 注意:
# 
# 
# 0 < s1.length, s2.length <= 1000。
# 所有字符串中的字符ASCII值在[97, 122]之间。
# 
# 
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int: ## 从后开始dp
        m,n = len(s1),len(s2)
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m-1,-1,-1):
            dp[i][n] = dp[i+1][n] + ord(s1[i])
        for j in range(n-1,-1,-1):
            dp[m][j] = dp[m][j+1] + ord(s2[j])
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j]+ord(s1[i]),dp[i][j+1]+ord(s2[j]))
                    
        return dp[0][0]


         
# @lc code=end
    # def minimumDeleteSum(self, s1: str, s2: str) -> int: 从前开始dp
    #     m,n = len(s1),len(s2)
        
    #     dp = [[0]*(n+1) for _ in range(m+1)]
        
    #     for i in range(1,m+1):
    #         dp[i][0] = dp[i-1][0] + ord(s1[i-1])
    #     for j in range(1,n+1):
    #         dp[0][j] = dp[0][j-1] + ord(s2[j-1])
            
    #     for i in range(1,m+1):
    #         for j in range(1,n+1):
    #             if s1[i-1] == s2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1] 
    #             else:
    #                 dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))
        
    #     return dp[-1][-1]
