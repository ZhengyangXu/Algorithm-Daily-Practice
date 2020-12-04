#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (32.37%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    48.7K
# Total Submissions: 149.8K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
# 
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
# 
# 
# 
# 示例 1：
# 
# 输入：
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 
# 
# 示例 2：
# 
# 输入：
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# 输出：[]
# 
# 
#

# @lc code=start
class Solution:
    from collections import Counter
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_num = len(words)
        str_len = len(s)
        ws_len = word_len * word_num  
        res = []
        
        for i in range(0,str_len-ws_len+1,word_len):
            counter = Counter(words)
            for j in range(i,ws_len,word_len):
                cur_word = s[j:j+word_len]
                if cur_word in counter:
                    counter[cur_word] -=1 
                
            
            
            
# @lc code=end





    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     numword = len(words)
    #     lenword = len(words[0])
    #     totallen = numword*lenword
    #     slen = len(s)
    #     i = 0 
    #     res = []
    #     while i <= slen - totallen:
    #         counter = Counter(words)
    #         for j in range(i,i+totallen,lenword):
    #             if s[j:j+lenword] in counter:
    #                 counter[s[j:j+lenword]] -= 1  
    #         if not any(counter.values()):
    #             res.append(i)
    #         i += 1 
    #     return res   
    ## 思路：愚蠢的暴力解。直接记数words,然后从头到尾比遍历s,若counter全为0则添加，否则不添加