#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (79.44%)
# Likes:    970
# Dislikes: 0
# Total Accepted:    191.6K
# Total Submissions: 241.1K
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0]
# 输出：[[],[0]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# nums 中的所有元素 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        n = len(nums)
        
        def backtrack(i,path):
            path = path[:]
            res.append(path)
            
            for k in range(i,n):
                path.append(nums[k])
                backtrack(k+1,path)
                path.pop()
        
        backtrack(0,[])
        

        return res  
            
# @lc code=end

    # def subsets(self, nums: List[int]) -> List[List[int]]:
        
    #     if not nums:
    #         return 
        
    #     size = len(nums)
    #     res = []
    #     def backtrack(i,path):
    #         res.append(path)
            
    #         for k in range(i,size):
    #             backtrack(k+1,path+[nums[k]])
        
    #     backtrack(0,[])
            
    #     return res 
    
    
    # def subsets(self, nums: List[int]) -> List[List[int]]:
        
    #     if not nums:
    #         return 
        
    #     size = len(nums)
    #     res = [[]]
    #     for i in nums:
    #         res += [[i] + num for num in res]

            
    #     return res 
            
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [] 
    #     n = len(nums)
        
    #     for mask in range(1<<n):
    #         path = []
    #         for i in range(n):
    #             if (mask & (1<<i)) != 0:
    #                 path.append(nums[i])
                    
    #         res.append(path)
    #     return res              