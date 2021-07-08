#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#
# https://leetcode-cn.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (41.28%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    22.4K
# Total Submissions: 42.5K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
# 
# 子数组 是数组的一段连续部分。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,0,1,0,1], goal = 2
# 输出：4
# 解释：
# 有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,0,0,0,0], goal = 0
# 输出：15
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# nums[i] 不是 0 就是 1
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        l1,l2,r = 0,0,0 
        s1,s2 =0,0 
        ret = 0 
        while r < n:
            s1 += nums[r]
            while l1 <= r and s1 > goal:
                s1 -= nums[l1]
                l1 += 1
            s2 += nums[r]
            while l2 <= r and s2 >= goal:
                s2 -= nums[l2]
                l2 += 1 
            ret += l2 - l1 
            r += 1 
        return ret      
# @lc code=end

def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    total = 0 
    cnt = defaultdict(int)
    ret = 0 
    for num in nums:
        cnt[total] += 1 
        total += num 
        ret += cnt[total - goal]
    return ret