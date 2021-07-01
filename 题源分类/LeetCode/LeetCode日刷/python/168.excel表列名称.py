#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (40.78%)
# Likes:    409
# Dislikes: 0
# Total Accepted:    67.9K
# Total Submissions: 161.4K
# Testcase Example:  '1'
#
# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
#
# 例如：
#
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
#
#
#
# 示例 1：
#
#
# 输入：columnNumber = 1
# 输出："A"
#
#
# 示例 2：
#
#
# 输入：columnNumber = 28
# 输出："AB"
#
#
# 示例 3：
#
#
# 输入：columnNumber = 701
# 输出："ZY"
#
#
# 示例 4：
#
#
# 输入：columnNumber = 2147483647
# 输出："FXSHRXW"
#
#
#
#
# 提示：
#
#
# 1
#
#
#


# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        dic = {}
        for i in range(26):
            dic[i] = chr(ord('A')+i)
            
        while columnNumber:
            columnNumber -= 1 
            ans += dic[columnNumber%26]
            columnNumber //= 26 
        return ans[::-1]


# @lc code=end

def convertToTitle(self, columnNumber: int) -> str:
    ans = ''
    while columnNumber > 0:
        columnNumber -= 1
        ans += chr(columnNumber % 26 + ord("A"))
        columnNumber //= 26
    return ans[::-1]