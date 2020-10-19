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
        left,right = 0,len(nums)-1 
        while left < right:
            mid = left + (right - left +1 ) // 2
            if nums[mid] == target:
                first,last = mid,mid 
                while nums[first-1] == target:
                    first -= 1 
                while nums[last-1] == target:
                    last += 1 
                return [first,last]
                
# @lc code=end

