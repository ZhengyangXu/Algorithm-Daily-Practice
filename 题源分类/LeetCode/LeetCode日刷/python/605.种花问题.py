#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
# https://leetcode-cn.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (34.11%)
# Likes:    306
# Dislikes: 0
# Total Accepted:    78.9K
# Total Submissions: 231.4K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
# 
# 给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n
# ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：flowerbed = [1,0,0,0,1], n = 1
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：flowerbed = [1,0,0,0,1], n = 2
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# flowerbed[i] 为 0 或 1
# flowerbed 中不存在相邻的两朵花
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool: ## 
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                    n -= 1
                else:
                    i += 1
            i += 2 
                    
            if n <= 0:
                return True 
        
        return False 
# @lc code=end

## 思路：考虑边际，第一朵和最后一朵，中间的如果前后两段都是0则可以种，种完之后就变成1。没有考虑[0]这种情况

    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool: ## 暴力解
        
    #     count = 0 
    #     size = len(flowerbed)

    #     for i in range(size):
    #         if flowerbed[i] == 0:
    #             if i == 0:
    #                 if size > 1:
    #                     if flowerbed[i+1] == 0:
    #                         count += 1
    #                         flowerbed[i] = 1
    #                 else:
    #                     count += 1
    #             elif i == size - 1:
    #                 if flowerbed[i-1] == 0:
    #                     count += 1 
    #                     flowerbed[i] = 1
                
    #             else:
    #                 if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
    #                     count += 1 
    #                     flowerbed[i] = 1 
                
    #     return count >= n
                
                
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool: ## 
        
    #     for i in range(len(flowerbed)):
    #         if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
    #             n -= 1 
    #             flowerbed[i] = 1 
    #             if n == 0:
    #                 break

                    
    #     return n <= 0