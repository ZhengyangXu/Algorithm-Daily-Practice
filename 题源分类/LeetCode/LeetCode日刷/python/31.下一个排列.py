#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (34.60%)
# Likes:    697
# Dislikes: 0
# Total Accepted:    94.5K
# Total Submissions: 273.1K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i,j,k = n-2,n-1,n-1   
        
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1 
            j -= 1 
            
        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1 
            nums[i],nums[k] = nums[i],nums[k]
        
        for i in range(j)
# @lc code=end

