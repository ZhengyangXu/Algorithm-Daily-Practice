#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (29.29%)
# Likes:    2558
# Dislikes: 0
# Total Accepted:    320K
# Total Submissions: 1.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue  
            if nums[i] > 0:
                break 
            l = i + 1 
            r = len(nums)-1 
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1 
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1 
                    l = l+1 
                    r = r-1
                elif sum > 0:
                    r -= 1 
                elif sum < 0:
                    l += 1 
        return res  
                               

                
            
# @lc code=end

