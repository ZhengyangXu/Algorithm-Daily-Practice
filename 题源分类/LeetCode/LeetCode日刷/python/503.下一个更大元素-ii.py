#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#
# https://leetcode-cn.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (57.70%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    32.7K
# Total Submissions: 56.7K
# Testcase Example:  '[1,2,1]'
#
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x
# 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
# 
# 示例 1:
# 
# 
# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数； 
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
# 
# 
# 注意: 输入数组的长度不会超过 10000。
# 
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        
        for i in range(n*2):
            while stack and nums[i%n]  > nums[stack[-1]]:
                res[stack.pop()] = nums[i%n]
                 
                   
            
            
            
            stack.append(i%n) 
            
        return res
    
                

# @lc code=end

# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
#         res = [-1] * len(nums)
#         stack = []
#         for i in range(len(nums)-1,-1,-1):
#             while stack and nums[i] >= nums[stack[-1]]:
#                 stack.pop()
                
#             if stack:
#                 res[i] = nums[stack[-1]]
            
#             stack.append(i)
            
#         for i in range(len(nums)-1,-1,-1):
#             while stack and nums[i] >= nums[stack[-1]]:
#                 stack.pop()  
#             if stack:
#                 res[i] = nums[stack[-1]]
                
#             stack.append(i)
#         return res   
    
    
# def nextGreaterElements(self, nums: List[int]) -> List[int]:
    
#     res = [-1] * len(nums)
#     stack = []
#     for i in range(len(nums)-1,-1,-1):
#         while stack and nums[i%len(nums)] >= nums[stack[-1]]:
#             stack.pop()
            
#         if stack:
#             res[i%(len(nums))] = nums[stack[-1]]
        
#         stack.append(i%(len(nums)))
    
#     return res   