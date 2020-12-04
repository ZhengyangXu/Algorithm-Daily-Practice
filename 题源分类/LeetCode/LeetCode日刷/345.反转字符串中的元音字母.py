#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (50.86%)
# Likes:    122
# Dislikes: 0
# Total Accepted:    52.3K
# Total Submissions: 102.7K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 
# 
# 
# 示例 1：
# 
# 输入："hello"
# 输出："holle"
# 
# 
# 示例 2：
# 
# 输入："leetcode"
# 输出："leotcede"
# 
# 
# 
# 提示：
# 
# 
# 元音字母不包含字母 "y" 。
# 
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aeiouAEIOU'
        l,r = 0,len(s)-1
        ans = list(s)
        while l < r:
            if s[l] not in vowel:
                l += 1
            if s[r] not in vowel:
                r -= 1 
            if s[l] in vowel and s[r] in vowel:
                ans[l],ans[r] = ans[r],ans[l]
                l += 1
                r -= 1 

        
        return ('').join(ans) 
        
# @lc code=end

