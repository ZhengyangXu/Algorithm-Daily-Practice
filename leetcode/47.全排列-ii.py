#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (59.58%)
# Likes:    371
# Dislikes: 0
# Total Accepted:    78.7K
# Total Submissions: 132.1K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,track,visited):
            if len(nums) == len(track):
                track = track[:]
                res.append(track)
            
            for i in range(len(nums)):
                if visited[i]:
                    continue  
                if i > 0 and nums[i] == nums[i-1] and visited[i-1]:
                    break 
                track.append(nums[i])
                visited[i] = True
                backtrack(nums,track,visited)
                track.pop()
                visited[i] = False  
            
        nums.sort()
        visited = [False]*len(nums)
        res = []
        track = []
        backtrack(nums,track,visited)
        return res
  
        
        

                
# @lc code=end
# def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#     def helper(nums,res,path):
#         if not nums and path not in res:
#             res.append(path)
        
#         for i in range(len(nums)):
#             helper(nums[:i]+nums[i+1:],res,path+[nums[i]])
#     res = []
#     helper(nums,res,[])
#     return res 

