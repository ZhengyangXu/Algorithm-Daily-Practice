#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (38.60%)
# Likes:    1212
# Dislikes: 0
# Total Accepted:    333.3K
# Total Submissions: 863.6K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        length = min(len(s) for s in strs)
        strs.sort(key=len)
        min_str = strs[0]
        l,r = 0,length 
        while l < r:
            mid = l + (r-l+1)//2 
            if all(min_str[:mid] == word[:mid] for word in strs[1:]):
                l = mid 
            else:
                r = mid - 1  
        return min_str[:l]
            
        
        

                
# @lc code=end
#   def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
#         for i in range(len(strs[0])):
#             for word in strs[1:]:
#                 if (i < len(word) and strs[0][i] != word[i]) or (i == len(word)):
#                     return strs[0][:i]
#         return strs[0]


# def longestCommonPrefix(self, strs: List[str]) -> str:
#     if not strs:
#         return ""
#     res = strs[0]
#     for word in strs[1:]:
#         while word.find(res) != 0:
#             res = res[:len(res)-1]
#     return res 

