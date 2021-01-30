#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#
# https://leetcode-cn.com/problems/nth-digit/description/
#
# algorithms
# Medium (38.87%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    12.8K
# Total Submissions: 32.9K
# Testcase Example:  '3'
#
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。
# 
# 
# 
# 注意：n 是正数且在 32 位整数范围内（n < 2^31）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：3
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
# 
# 
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n  
        
        base = 9
        digits = 1 
        
        while n - base * digits > 0:
            n -= base * digits 
            base *= 10 
            digits += 1 
            
        index = n % digits  
        if index == 0:
            num = 10 ** (digits-1) + n // digits - 1 
            
            return num % 10 
        else:
            num = 10 ** (digits-1) + n//digits 
            for i in range(index,digits):
                num //= 10 
            return num % 10 
# @lc code=end

