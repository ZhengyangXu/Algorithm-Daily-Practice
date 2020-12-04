#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (30.85%)
# Likes:    2391
# Dislikes: 0
# Total Accepted:    308.9K
# Total Submissions: 997.6K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划
        size = len(s)
        if size < 2:
            return s 
        max_len = 1 
        dp = [[False for _ in range(size)] for _ in range(size)]
        start = 0 
        
        for j in range(1,size):
            for i in range(0,j):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i+1][j-1])
                
                if dp[i][j]:
                    cur_len = j - i + 1 
                    if cur_len > max_len:
                        max_len = cur_len  
                        start = i 
        return s[start:start+max_len]
                    
        
  
                
# @lc code=end

      # def isP(s,left,right): 中心扩散算法
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1 
        #         right += 1 
        #     return s[left+1:right]
        # ans = ''
        # for i in range(len(s)):
        #     par1 = isP(s,i,i)
        #     if len(par1) > len(ans):
        #         ans = par1 
        #     par2 =isP(s,i,i+1)
        #     if len(par2) > len(ans):
        #         ans = par2 
        # return ans 