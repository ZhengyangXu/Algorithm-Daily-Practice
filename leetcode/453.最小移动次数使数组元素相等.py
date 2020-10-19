#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minnum = min(nums)
        res = 0
        for i in nums:
            if i != minnum:
                res += i - minnum 
        return res

        
# @lc code=end


