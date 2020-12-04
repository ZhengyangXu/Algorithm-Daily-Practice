#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (52.87%)
# Likes:    1827
# Dislikes: 0
# Total Accepted:    167.9K
# Total Submissions: 315.4K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 
# 
# 示例 2：
# 
# 
# 输入：height = [4,2,0,3,2,5]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# n == height.length
# 0 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int: ## 双指针
        if not height:
            return 0 
        n = len(height)
        left,right = 0,n-1 
        lmax = height[0] 
        rmax = height[n-1]
        res = 0 
        while left <= right:
            lmax = max(height[left],lmax)
            rmax = max(height[right],rmax)
            
            if lmax < rmax:
                res += lmax - height[left]
                left += 1
            else:
                res += rmax - height[right]
                right -= 1
        return res 

                
# @lc code=end
    # def trap(self, height: List[int]) -> int: ## 暴力解超时
    #     if not height:
    #         return 0 
    #     size = len(height)
        
    #     res = 0
    #     for i in range(1,size-1):
    #         lmax,rmax = 0,0 
    #         for j in range(i,-1,-1):
    #             lmax = max(height[j],lmax)
                
    #         for j in range(i,size):
    #             rmax = max(height[j],rmax)
                
    #         res += min(lmax,rmax) - height[i] 
            
        
    #     return res
    # def trap(self, height: List[int]) -> int: ## 备忘录
    #     if not height:
    #         return 0 
    #     size = len(height)
        
    #     res = 0
    #     lmax = [0]*size 
    #     rmax = [0]*size
    #     lmax[0] = height[0]
    #     rmax[size-1] = height[size-1]
    #     for i in range(1,size):
    #         lmax[i] = max(lmax[i-1],height[i])
        
    #     for j in range(size-2,-1,-1):
    #         rmax[j] = max(rmax[j+1],height[j])
            
    #     for k in range(1,size):
    #         res += min(rmax[k],lmax[k]) - height[k]
            
    #     return res