#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (38.57%)
# Likes:    701
# Dislikes: 0
# Total Accepted:    72K
# Total Submissions: 186K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。
# 
# 
# 
# 示例：
# 
# 输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC"
# 
# 
# 
# 提示：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution:
    from collections import Counter 
    def minWindow(self, s: str, t: str) -> str:
        r,l = 0,0 
        needcnt = len(t)
        need = Counter(t)
        min_len = float('inf')
        res = ''
        while r < len(s):
            if need[s[r]] > 0:
                needcnt -= 1 
            need[s[r]] -= 1 
            r += 1   
            while needcnt == 0:
                if r - l < min_len:
                    min_len = r - l  
                    res = s[l:r]
                if need[s[l]] == 0:
                    needcnt += 1  
                need[s[l]] += 1 
                l += 1 
        return res 

# @lc code=end
#  def minWindow(self, s: str, t: str) -> str:
#         l,r = 0,0   
#         res = ''
#         min_len = float('inf')
#         need = Counter(t)
#         needcnt = len(t)
        
#         while r < len(s):
#             if need[s[r]] > 0:
#                 needcnt -= 1  
#             need[s[r]] -= 1 
#             r += 1  
#             while needcnt == 0:
#                 if r - l < min_len:
#                     min_len = r - l  
#                     res = s[l:r]    
#                 if need[s[l]] == 0:
#                     needcnt += 1    
#                 need[s[l]] += 1  
#                 l += 1 
#         return res   
