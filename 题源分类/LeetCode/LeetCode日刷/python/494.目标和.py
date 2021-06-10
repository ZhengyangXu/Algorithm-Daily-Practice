#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (46.15%)
# Likes:    756
# Dislikes: 0
# Total Accepted:    105.5K
# Total Submissions: 218.3K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 target 。
#
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
#
#
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
#
# 示例 2：
#
#
# 输入：nums = [1], target = 1
# 输出：1
#
#
#
#
# 提示：
#
#
# 1
# 0
# 0
# -1000
#
#
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        res = 0 
        for num in nums:
            res += num 
        diff = res - target 
        if diff < 0 or diff % 2 != 0:
            return 0 
        
        n = len(nums)
        neg = diff//2 
        
        dp =[[0] * (neg+1) for _ in range(n+1)]
        dp[0][0] = 1 
        for i in range(1,n+1):
            num = nums[i-1]
            for j in range(neg+1):
                dp[i][j] = dp[i-1][j] 
                if (j >= num):
                    dp[i][j] += dp[i-1][j-num]
                    
        return dp[n][neg]

# @lc code=end

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        count = 0
        n = len(nums)
        def backtrack(nums,path):
            nonlocal count
            if len(path) == n and sum(path) == target:
                count += 1

            for i in range(len(nums)):
                for symbol in ('-','+'):
                    path.append(int(symbol+str(nums[i])))
                    backtrack(nums[i+1:],path)
                    path.pop()
        backtrack(nums,[])
        return count
    ### 超时
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        count = 0
        n = len(nums)

        def backtrack(nums, index, res):
            nonlocal count
            if n == index:
                if res == target:
                    count += 1
            else:
                backtrack(nums, index + 1, res + nums[index])
                backtrack(nums, index + 1, res - nums[index])

        backtrack(nums, 0, 0)
        return count
