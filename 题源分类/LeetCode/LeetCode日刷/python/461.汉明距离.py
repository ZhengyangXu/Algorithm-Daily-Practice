#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#
# https://leetcode-cn.com/problems/hamming-distance/description/
#
# algorithms
# Easy (79.21%)
# Likes:    459
# Dislikes: 0
# Total Accepted:    137K
# Total Submissions: 170K
# Testcase Example:  '1\n4'
#
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
# 
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
# 
# 注意：
# 0 ≤ x, y < 2^31.
# 
# 示例:
# 
# 
# 输入: x = 1, y = 4
# 
# 输出: 2
# 
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# 
# 上面的箭头指出了对应二进制位不同的位置。
# 
# 
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        z = x ^ y 
        while z:
            z &= z-1 
            count += 1 
        return count 
            
# @lc code=end

    # def hammingDistance(self, x: int, y: int) -> int:
    #     count = 0
    #     for i in range(32):
    #         if x & 1 != y & 1:
    #             count += 1 
    #         x >>= 1 
    #         y >>= 1 
    #     return count 
    
    # def hammingDistance(self, x: int, y: int) -> int:
        # count = 0
        # z = x ^ y 
        # for i in range(32):
        #     if z & 1:
        #         count += 1 
        #     z >>= 1 
        # return count 
        
    # def hammingDistance(self, x: int, y: int) -> int:
    #     count = 0
    #     z = x ^ y 
    #     while z:
    #         count += z & 1 
    #         z >>= 1 
    #     return count 