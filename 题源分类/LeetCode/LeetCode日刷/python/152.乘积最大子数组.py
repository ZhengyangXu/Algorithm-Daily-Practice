#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (41.18%)
# Likes:    987
# Dislikes: 0
# Total Accepted:    124.9K
# Total Submissions: 303.1K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
#
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curP = 1
        minP = 1
        maxN = float("-inf")
        res = float("-inf")

        for num in nums:
            curP *= num
            if curP > 0:
                res = max(res, curP // minP)
                minP = min(minP, curP)
            elif curP < 0:
                if maxN != float("-inf"):
                    res = max(res, curP // maxN)
                else:
                    res = max(res, num)
                maxN = max(maxN, curP)
            else:
                curP = 1
                minP = 1
                maxN = float("-inf")
                res = max(res, num)
        return res


# @lc code=end

# def maxProduct(self, nums: List[int]) -> int:
#     n = len(nums)

#     res = nums[0]
#     preMax = nums[0]
#     preMin = nums[0]

#     for i in range(1, n):
#         curMax = max(preMax * nums[i], preMin * nums[i], nums[i])
#         curMin = min(preMax * nums[i], preMin * nums[i], nums[i])
#         res = max(res, curMax)
#         preMax = curMax
#         preMin = curMin
#     return res

# def maxProduct(self, nums: List[int]) -> int:
#     reverseNums = nums[::-1]
#     for i in range(1, len(nums)):
#         nums[i] *= nums[i - 1] or 1
#         reverseNums[i] *= reverseNums[i - 1] or 1
#     return max(nums + reverseNums)
