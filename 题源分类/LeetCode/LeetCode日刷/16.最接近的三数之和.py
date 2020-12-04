#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.81%)
# Likes:    564
# Dislikes: 0
# Total Accepted:    151.1K
# Total Submissions: 329.6K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 
# 
# 示例：
# 
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not nums or n < 3:
            return None  
        ans = float('inf')
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  
            l,r = i+1,n-1 
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(sum-target) <= abs(ans-target):
                    ans = sum  
                if sum > target:
                    r -= 1 
                if sum < target:
                    l += 1
                if sum == target:
                    return sum 
        return ans 
# @lc code=end

