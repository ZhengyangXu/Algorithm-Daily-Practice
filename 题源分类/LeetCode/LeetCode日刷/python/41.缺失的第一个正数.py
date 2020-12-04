#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (40.32%)
# Likes:    866
# Dislikes: 0
# Total Accepted:    99.3K
# Total Submissions: 246.3K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
# 
# 
# 
# 示例 1:
# 
# 输入: [1,2,0]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [3,4,-1,1]
# 输出: 2
# 
# 
# 示例 3:
# 
# 输入: [7,8,9,11,12]
# 输出: 1
# 
# 
# 
# 
# 提示：
# 
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
# 
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1  
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1 
                
        
        for i in range(n):
            num = abs(nums[i])
            
            if num <= n:
                nums[num-1] = -abs(nums[num-1])

        for i in range(n):
            if nums[i] > 0:
                return i+ 1 
        
        return n+1        
            
# @lc code=end

## 思路：原地修改数组，使得数组下标和下标位置的值一一对应。比如1放在下标为0的位置，
## 2放在下标为一的位置，相当于哈希表。这里需要注意的是，只有nums[i]在1到N范围之内
## 才能寻找合适的位置，如果当前值大于N，则在数组里找不到合适的位置，那么最小的正整数
## 肯定是比这个数小的数。

    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 1  
        
    #     size = len(nums)
        
    #     for i in range(size):
    #         while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
    #             nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        
    #     for i in range(size):
    #         if i+1 != nums[i]:
    #             return i + 1 
        
    #     return size + 1 