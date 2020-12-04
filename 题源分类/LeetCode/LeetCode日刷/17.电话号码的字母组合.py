#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (55.41%)
# Likes:    908
# Dislikes: 0
# Total Accepted:    174.2K
# Total Submissions: 314.2K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 示例:
# 
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
# 
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:## 递归
        if not digits:
            return []
        phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}
        def dfs(index,temp):
            if index == len(digits):
                res.append(temp)
                return 
            for letter in phoneMap[digits[index]]:
                dfs(index+1,temp+letter)
        res = []
        dfs(0,'')
        return res   
  
        

# @lc code=end

    # def letterCombinations(self, digits: str) -> List[str]: 回溯
    #     if not digits:
    #         return []
    #     d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    #     def backtrack(index,path):
    #         if len(path) == len(digits):
    #             path = path[:]
    #             res.append(path) 
    #         else:
    #             digit = d[int(digits[index])]
    #             for letter in digit:
    #                 path += letter
    #                 backtrack(index+1,path)
    #                 path = path[:-1]
    #     res = []
    #     path = ''
    #     backtrack(0,path)
    #     return res    

    # def letterCombinations(self, digits: str) -> List[str]:## 队列
    #     if not digits:
    #         return []
    #     d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    #     res = []
    #     queue = ['']
    #     for index in digits:
    #         digit = int(index)
    #         for _ in range(len(queue)):
    #             tmp = queue.pop(0)
    #             for letter in d[digit]:
    #                 queue.append(tmp+letter)
    #     return queue   