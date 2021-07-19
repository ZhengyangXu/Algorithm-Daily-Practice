#
# @lc app=leetcode.cn id=1838 lang=python3
#
# [1838] 最高频元素的频数
#
# https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element/description/
#
# algorithms
# Medium (38.24%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    17K
# Total Submissions: 40.4K
# Testcase Example:  '[1,2,4]\n5'
#
# 元素的 频数 是该元素在一个数组中出现的次数。
# 
# 给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。
# 
# 执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,4], k = 5
# 输出：3
# 解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
# 4 是数组中最高频元素，频数是 3 。
# 
# 示例 2：
# 
# 
# 输入：nums = [1,4,8,13], k = 5
# 输出：2
# 解释：存在多种最优解决方案：
# - 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
# - 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
# - 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [3,9,6], k = 2
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = ans = 0 
        for j,num in enumerate(nums):
            k += num 
            while k < num * (j - i + 1):
                k -= nums[i]
                i += 1 
            ans = max(ans,j-i+1)
        return ans 
    # @lc code=end

    # def maxFrequency(self, nums: List[int], k: int) -> int:
    #     nums.sort() 
    #     n = len(nums)
    #     def dif(nums):
    #         return [nums[len(nums)-1] - nums[i] for i in range(len(nums)-1)]

    #     maxcount = 1 
    #     for i in range(n-1,0,-1):
    #         p = k 
    #         diff = dif(nums[:i+1])
    #         diff=diff[::-1]
    #         for j in range(len(diff)): 
    #             p -= diff[j]
    #             if p < 0:
    #                 maxcount = max(maxcount,i -j)
    #         if p >= 0:
    #             maxcount = max(maxcount,i+1)
    #     return maxcount
    
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort() 
        i = j = 0 
        for j,num in enumerate(nums):
            k += num 
            if k < num * (j - i + 1):
                k -= nums[i] 
                i += 1 
        return j - i + 1 
    
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = ans = 0 
        for j,num in enumerate(nums):
            k += num 
            while k < num * (j - i + 1):
                k -= nums[i]
                i += 1 
            ans = max(ans,j-i+1)
        return ans 