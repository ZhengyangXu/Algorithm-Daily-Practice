#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (62.60%)
# Likes:    797
# Dislikes: 0
# Total Accepted:    230.2K
# Total Submissions: 367.5K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return  
        i = 0 
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1 
        for k in range(i,len(nums)):
            nums[k] = 0 
        return nums 
                
# @lc code=end

## 思路：双指针，相当于27题，当val = 0 时，最后nums[i:]赋0值即可