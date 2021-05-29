#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.45%)
# Likes:    918
# Dislikes: 0
# Total Accepted:    114.3K
# Total Submissions: 256.3K
# Testcase Example:  '[1,1,1]\n2'
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#
#
# 说明 :
#
#
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
#
#
#


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        if not nums:
            return 0
        ans = 0
        for i in range(len(nums)):
            presum = 0
            for j in range(i, -1, -1):
                presum += nums[j]
                if presum == k:
                    ans += 1
        return ans


# @lc code=end

# def subarraySum(self, nums: List[int], k: int) -> int:

#     if not nums:
#         return 0
#     pre = 0
#     dic = {0:1}
#     ans = 0
#     for i in range(len(nums)):
#         pre += nums[i]
#         if pre - k in dic:
#             ans += dic[pre-k]
#         dic[pre]  = dic[pre] + 1 if pre in dic else 1
#     return ans
