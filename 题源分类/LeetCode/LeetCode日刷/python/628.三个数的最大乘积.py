#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (52.23%)
# Likes:    296
# Dislikes: 0
# Total Accepted:    72.4K
# Total Submissions: 138.7K
# Testcase Example:  '[1,2,3]'
#
# 给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：6
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,4]
# 输出：24
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [-1,-2,-3]
# 输出：-6
# 
# 
# 
# 
# 提示：
# 
# 
# 3 
# -1000 
# 
# 
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0 
        max1,max2,max3 = -float('inf'),-float('inf'),-float('inf')
        min1,min2 = float('inf'),float('inf')
        
        for i in range(len(nums)):
            if nums[i] > max1:
                max3 = max2 
                max2 = max1 
                max1 = nums[i] 
            elif nums[i] > max2:
                max3 = max2 
                max2 = nums[i] 
            elif nums[i] > max3:
                max3 = nums[i]
            
            if nums[i] < min1:
                min2 = min1 
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
                
        return max(max1*max2*max3,max1*min1*min2)
                
        
        
        
        
        
        
        # @lc code=end
    # def maximumProduct(self, nums: List[int]) -> int: 时间复杂度 0(nlogn)
    #     if len(nums) < 3:
    #         return 0 
    #     nums.sort()
    #     if nums[0] >= 0 or nums[-1] <= 0:
    #         return nums[-3]*nums[-2]*nums[-1]
    #     else:
    #         return max(nums[0]*nums[1]*nums[-1],nums[-3]*nums[-2]*nums[-1])
