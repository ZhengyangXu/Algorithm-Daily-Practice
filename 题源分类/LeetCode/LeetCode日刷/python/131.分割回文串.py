#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (70.43%)
# Likes:    629
# Dislikes: 0
# Total Accepted:    89.4K
# Total Submissions: 122.8K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 
# 回文串 是正着读和反着读都一样的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a"
# 输出：[["a"]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPlain(s):
            if s[::-1] == s:
                return True  
            return False
        
        def backtrack(s,res,path):
            if not s:
                res.append(path)
                return  
            
            for i in range(1,len(s)+1):
                if isPlain(s[:i]):
                    backtrack(s[i:],res,path+[s[:i]])
                    
        res = []
        backtrack(s,res,[])
        return res 
        
        
# @lc code=end

