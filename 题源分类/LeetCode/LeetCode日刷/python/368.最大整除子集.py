#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#
# https://leetcode-cn.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (40.34%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 59.6K
# Testcase Example:  '[1,2,3]'
#
# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i],
# answer[j]) 都应当满足：
# 
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 
# 
# 如果存在多个有效解子集，返回其中任何一个均可。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# nums 中的所有整数 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n 
        maxsize = 1 
        maxval = dp[0]
        
        for i in range(1,n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i],dp[j]+1)
            if dp[i] > maxsize:
                maxsize = dp[i]
                maxval = nums[i]
                
        res = []
        if maxsize == 1:
            res.append(nums[0])
            return res 
        i = n- 1 
        while i >=0 and maxsize >0:
            if dp[i] == maxsize and maxval % nums[i] == 0:
                res.append(nums[i])
                maxval = nums[i]
                maxsize -= 1
            i -= 1 
        return res 
# @lc code=end

