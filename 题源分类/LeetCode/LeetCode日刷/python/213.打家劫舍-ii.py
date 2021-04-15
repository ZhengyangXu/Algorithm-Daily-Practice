#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# https://leetcode-cn.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (41.38%)
# Likes:    598
# Dislikes: 0
# Total Accepted:    105.1K
# Total Submissions: 249.9K
# Testcase Example:  '[2,3,2]'
#
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈
# ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0 
        if len(nums) == 1:
            return nums[0]


        def dprob(nums):
            if not nums:
                return 0 
            n = len(nums)
            if n < 2:
                return nums[0]
            dp = [0]*n  
            dp[0] = nums[0]
            dp[1] = max(nums[1],nums[0])
            
            for i in range(2,n):
                dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            return dp[-1] 
        return max(dprob(nums[1:len(nums)]),dprob(nums[:len(nums)-1]))
# @lc code=end

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def simple_rob(nums):
#             rob,not_rob=0,0
#             for num in nums:
#                 rob,not_rob = not_rob+num,max(rob,not_rob)
#             return max(rob,not_rob)
        
#         if not nums:
#             return 0 
#         elif len(nums) == 1:
#             return nums[0]
#         else:
#             return max(simple_rob(nums[1:]),simple_rob(nums[:-1]))