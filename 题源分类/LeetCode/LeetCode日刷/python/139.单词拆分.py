#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (49.95%)
# Likes:    992
# Dislikes: 0
# Total Accepted:    146.7K
# Total Submissions: 292.3K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not s or not wordDict:
            return True 
        n = len(s)
        @functools.lru_cache(None)
        def backtrack(s):
            if not s:
                return True 
            res = False 
            
            for i in range(1,len(s)+1):
                if s[:i] in wordDict:
                    res = backtrack(s[i:]) or res 
            return res 
        return backtrack(s)
         
        
# @lc code=end

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     n = len(s)
    #     dp = [False for _ in range(n+1)]
    #     dp[0] = True 
    #     for i in range(n+1):
    #         for j in range(i+1,n+1):
    #             if dp[i] and s[i:j] in wordDict:
    #                 dp[j] = True 
    #     return dp[-1]
        