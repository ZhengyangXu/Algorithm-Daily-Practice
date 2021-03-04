#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (47.69%)
# Likes:    1401
# Dislikes: 0
# Total Accepted:    214K
# Total Submissions: 448.8K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7]
# 的子序列。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^4 
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以设计时间复杂度为 O(n^2) 的解决方案吗？
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        n = len(nums)
        tail = [nums[0]]
        
        for i in range(1,n):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue 
        
            left,right = 0,len(tail)-1
            while left < right:
                mid = (left+right)>>1
                if tail[mid] < nums[i]:
                    left = mid + 1 
                else:
                    right = mid  
            tail[left] = nums[i]
        return len(tail)
                
# @lc code=end

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0 
        
    #     n = len(nums)

    #     f = [1]*n
    #     for i in range(1,n):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 f[i] = max(f[j] + 1,f[i])
                    
    #     return max(f)