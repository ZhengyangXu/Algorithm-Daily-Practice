#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (35.83%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    27.8K
# Total Submissions: 77.5K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
# 
# 示例1:
# 
# 
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
# 
# 
# 
# 
# 示例2:
# 
# 
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
# 
# 
# 
# 
# 注意：
# 
# 
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
# 
# 
#

# @lc code=start
class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0,0   
        needcnt = len(s1)
        need =  Counter(s1)
        while r < len(s2):
            if need[s2[r]] > 0:
                needcnt -= 1  
            need[s2[r]] -= 1 
            r += 1  
            while needcnt == 0:
                if r-l == len(s1):
                    return True  
                if need[s2[l]] == 0:
                    needcnt += 1      
                need[s2[l]] += 1 
                l += 1 
        return False 
             
# @lc code=end

