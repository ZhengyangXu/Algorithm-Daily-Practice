#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (35.37%)
# Likes:    4192
# Dislikes: 0
# Total Accepted:    621K
# Total Submissions: 1.8M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    from collections import Counter
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0  
        l,r = 0,0 
        res = 0 
        window = Counter()
        while r  < len(s):
            c1 = s[r]
            window[c1] += 1  
            r += 1  
            while window[c1] > 1:
                c2 = s[l]
                window[c2] -= 1  
                l += 1 
            res = max(res,r-l)
        return res 
        
    
            
  
                    
# @lc code=end
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     l,r = 0,0 
    #     res = 0 
         
    #     window = Counter()
    #     while r < len(s):
    #         c1 = s[r]
    #         window[c1] += 1  
    #         r += 1 
    #         while window[c1] > 1:
    #             c2 = s[l]
    #             window[c2] -= 1 
    #             l += 1 
    #         res = max(res,r-l)
    #     return res
    
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     l,r = 0,0 
    #     res = 0
    #     window = [] 
    #     while r < len(s):
    #         if s[r] not in window: 
    #             window.append(s[r])
    #             r += 1 
    #         else: 
    #             while s[r] in window:  
    #                 window.pop(0)
    #                 l += 1   
    #         res = max(res,r-l)
    #     return res      
