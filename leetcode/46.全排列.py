#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.62%)
# Likes:    834
# Dislikes: 0
# Total Accepted:    169.1K
# Total Submissions: 220.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 1:
            return [nums]   
        for y in range(len(nums)):
            for j in self.permute(nums[:y]+nums[y+1:]):
                 res.append([nums[y]]+j)
            
        return res
 

            
# @lc code=end
    #    result = []
    #     def backtrack(nums,track):
    #         if len(nums) == len(track):
    #             track = track[:]
    #             result.append(track)
                
    #         for num in nums:
    #             if num in track:
    #                 continue  
    #             track.append(num)
    #             backtrack(nums,track)
    #             track.pop()
    #     track = []
    #     backtrack(nums,track)
    #     return result 

