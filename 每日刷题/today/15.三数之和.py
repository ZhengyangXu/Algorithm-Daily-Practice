#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (35.22%)
# Likes:    4662
# Dislikes: 0
# Total Accepted:    926.3K
# Total Submissions: 2.6M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
# 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#
#
# 示例 2：
#
#
# 输入：nums = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：nums = [0]
# 输出：[]
#
#
#
#
# 提示：
#
#
# 0
# -10^5
#
#
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # list
        nums.sort()
        n = len(nums)
        for l in range(n - 2):
            if l > 0 and nums[l - 1] == nums[l]:
                continue

            target = -nums[l]
            r = n - 1

            for m in range(l + 1, r):
                if m > l + 1 and nums[m] == nums[m - 1]:
                    continue

                while m < r and nums[m] + nums[r] > target:
                    r -= 1

                if m == r:
                    break

                if nums[m] + nums[r] == target:
                    res.append([nums[l], nums[m], nums[r]])

        return res


# @lc code=end

# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     res = []
#     nums.sort()
#     n = len(nums)
#     for l in range(n - 2):
#         if l > 0 and nums[l] == nums[l - 1]:
#             continue

#         m, r = l + 1, n - 1

#         while m < r:
#             s = nums[l] + nums[m] + nums[r]
#             if s < 0:
#                 m += 1
#             elif s > 0:
#                 r -= 1
#             else:
#                 res.append([nums[l], nums[m], nums[r]])
#                 while m < r and nums[m] == nums[m + 1]:
#                     m += 1
#                 while m < r and nums[r] == nums[r - 1]:
#                     r -= 1
#                 m += 1
#                 r -= 1
#     return res
# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     res = []
#     nums.sort()
#     n = len(nums)
#     for l in range(n - 2):
#         if l > 0 and nums[l] == nums[l - 1]:
#             continue
#         target = -nums[l]
#         r = n - 1

#         for m in range(l + 1, r):
#             if m > l + 1 and nums[m] == nums[m - 1]:
#                 continue
#             while m < r and nums[m] + nums[r] > target:
#                 r -= 1
#             if m == r:
#                 break
#             if nums[m] + nums[r] == target:
#                 res.append([nums[l], nums[m], nums[r]])
#     return res
