#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (39.96%)
# Likes:    522
# Dislikes: 0
# Total Accepted:    114.4K
# Total Submissions: 285.9K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 如果数组中不存在目标值，返回 [-1, -1]。
# 
# 示例 1:
# 
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 
# 示例 2:
# 
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        def last(nums,target,right):

            
            low,high = -1,len(nums)-1
            
            while low < high:
                mid = low + (high-low+1)//2 
                if nums[mid] < target or (right and nums[mid] == target):
                    low = mid  
                else:
                    high = mid - 1 
            return high  
        
        right = last(nums,target,True)
        if right == len(nums) or nums[right] != target:
            return [-1,-1]
        
        return [last(nums,target,False)+1,last(nums,target,True)]

 
                
# @lc code=end

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     if len(nums) == 0:
    #         return[-1,-1]
    #     if len(nums) == 1 and target == nums[0]:
    #         return [0,0]

    #     def first(nums,target):

    #         low,high = 0,len(nums)-1
    #         while low < high:
    #             mid = low + (high-low)//2
    #             if nums[mid] == target:
    #                 if nums[mid-1] < target:
    #                     return mid
    #                 else:
    #                     high = mid  
    #                     continue 
    #             elif nums[mid] < target:
    #                 low = mid + 1
    #             else:
    #                 high = mid 
    #         if nums[low] == target:
    #             return low
    #         return -1 
    #     def last(nums,target):

    #         low,high = 0,len(nums)-1
    #         while low < high:
    #             mid = low + (high-low+1)//2
    #             if nums[mid] == target:
    #                 if mid == high or nums[mid+1] > target:
    #                     return mid
    #                 else:
    #                     low = mid  
    #                     continue 
    #             elif nums[mid] > target:
    #                 high = mid - 1 
    #             else:
    #                 low = mid
    #         if nums[high] == target:
    #             return high 
    #         return -1 
    #     left = first(nums,target)
    #     right = last(nums,target)
        
    #     if left != -1 and right == -1:
    #         return [left,left]
    #     elif left == -1 and right != -1:
    #         return [right,right]
    #     else:
    #         return [left,right]
    #思路：这种解法corner case太多了，错了n次。就是用二分法找左右等于target的index，左边的就是左中位数，
    #右边的就是有中位数。要注意考虑left=right的特殊解情况，这种解法太长了，思路和官方题解一样，但是官方
    #题解短得多。
    
    
        # def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if not nums:
        #     return [-1,-1]
        # def first(nums,target,left):

            
        #     low,high = 0,len(nums)
            
        #     while low < high:
        #         mid = low + (high-low)//2 
        #         if nums[mid] > target or (left and nums[mid] == target):
        #             high = mid  
        #         else:
        #             low = mid + 1 
        #     return low  
        
        # left = first(nums,target,True)
        # if left == len(nums) or nums[left] != target:
        #     return [-1,-1]
        
        # return [left,first(nums,target,False)-1]