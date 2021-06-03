#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#
# https://leetcode-cn.com/problems/contiguous-array/description/
#
# algorithms
# Medium (45.78%)
# Likes:    367
# Dislikes: 0
# Total Accepted:    28.7K
# Total Submissions: 55.2K
# Testcase Example:  '[0,1]'
#
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
#
#
#
# 示例 1:
#
#
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
#
# 示例 2:
#
#
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
#
#
#
# 提示：
#
#
# 1
# nums[i] 不是 0 就是 1
#
#
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0]
        for i in range(n):
            presum.append(presum[-1] + (1 if nums[i] else -1) )
        
        dic = {0:0}
        ans = 0
        for i in range(2,len(presum)):
            if presum[i-2] not in dic:
                dic[presum[i-2]] = i- 2
            if presum[i] in dic:
                ans = max(ans,i-dic[presum[i]])
            
            
        
        return ans 
# @lc code=end

    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        count = ans = 0
        dic = {0: -1}

        for i, num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1

            if count in dic:
                ans = max(ans, i - dic[count])
            else:
                dic[count] = i
        return ans
