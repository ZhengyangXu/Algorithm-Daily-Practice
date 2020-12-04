#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode-cn.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (65.73%)
# Likes:    784
# Dislikes: 0
# Total Accepted:    87.1K
# Total Submissions: 132.4K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和
# n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
# 
# 示例 1:
# 
# 输入: [1,3,4,2,2]
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [3,1,3,4,2]
# 输出: 3
# 
# 
# 说明：
# 
# 
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n^2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        assert len(nums) > 1
        l = 1 
        r = len(nums) - 1 
        
        while l < r:
            mid = l + (r-l+1)//2 
            counter = 0 
            for num in nums:
                if num < mid:
                    counter += 1 
            if counter < mid:
                l = mid  
            else:
                assert counter >= mid  
                r = mid - 1 
        return l 
        
# @lc code=end

