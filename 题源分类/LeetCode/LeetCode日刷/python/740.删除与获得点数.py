#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除与获得点数
#
# https://leetcode-cn.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (54.12%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    23.9K
# Total Submissions: 39.6K
# Testcase Example:  '[3,4,2]'
#
# 给你一个整数数组 nums ，你可以对它进行一些操作。
# 
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] +
# 1 的元素。
# 
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    from collections import Counter
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        def rob(dp):
            n = len(dp)
            if n == 1:
                return dp[0]
            first,second = dp[0],max(dp[1],dp[0])
            
            for i in range(2,n):
                first,second = second,max(dp[i]+first,second)
                
            return second
            
                
        nums.sort()
        n = len(nums)
        total = [nums[0]]
        ans = 0
        for i in range(1,n):
            val = nums[i]
            if val == nums[i-1]:
                total[-1] += val 
            elif val == nums[i-1]+1:
                total.append(val)
            else:
                ans += rob(total)
                total = [val]
                
        ans += rob(total)
        return ans 
        
# @lc code=end

    # def deleteAndEarn(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0 
        
    #     maxvalue = max(nums)
    #     dp = [0] * (maxvalue+1)
    #     for num in nums:
    #         dp[num] += num 
    #     n = len(dp)
    #     first,second = dp[0],max(dp[1],dp[0])
    #     for i in range(2,n):
    #         first,second = second,max(dp[i]+first,second)
        
    #     return second 