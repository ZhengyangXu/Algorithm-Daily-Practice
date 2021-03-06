#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#
# https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (50.48%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    11.1K
# Total Submissions: 21.8K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
# 
# 
# 
# 示例：
# 
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
# 
# 
# 
# 
# 提示：
# 
# 
# 给定单词的长度不超过500。
# 给定单词中的字符只含有小写字母。
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m,n = len(word1),len(word2)

        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return m+n-2*dp[m][n]
        
# @lc code=end
## 思路：找到最长公共子串，然后原字符长度减去公共子串长度就是需要的操作数 
