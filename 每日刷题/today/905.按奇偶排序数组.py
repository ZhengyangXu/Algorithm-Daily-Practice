#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#
# https://leetcode-cn.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (70.00%)
# Likes:    289
# Dislikes: 0
# Total Accepted:    92.3K
# Total Submissions: 129.8K
# Testcase Example:  '[3,1,2,4]'
#
# 给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。
#
# 返回满足此条件的 任一数组 作为答案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,1,2,4]
# 输出：[2,4,3,1]
# 解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
#
#
#


# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        ## 双指针
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 == 1:
                r -= 1

            if l < r and nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return nums


# @lc code=end
# def sortArrayByParity(self, nums: List[int]) -> List[int]:

#     ## 双指针原地交换
#     i, j = 0, len(nums) - 1

#     while i < j:
#         while i < j and nums[j] % 2 == 1:
#             j -= 1
#         while i < j and nums[i] % 2 == 0:
#             i += 1
#         if i < j:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#             j -= 1
#     return nums
# def sortArrayByParity(self, nums: List[int]) -> List[int]:

#     ## 一次遍历
#     n = len(nums)
#     res = [0] * n
#     l, r = 0, n - 1

#     for num in nums:
#         if num % 2 == 0:
#             res[l] = num
#             l += 1
#         else:
#             res[r] = num
#             r -= 1
#     return res
