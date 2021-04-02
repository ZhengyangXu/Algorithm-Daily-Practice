#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (61.67%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    64.4K
# Total Submissions: 104.3K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        n = len(nums)
        nums.sort()
        def backtrack(i,path): ## 排序去重
   
            if path not in res:
                res.append(path)
            
            for k in range(i,n):
                backtrack(k+1,[nums[k]]+path)
                
        
        
        # def backtrack2(i,n,path):
        #     res.append(path)
            
        #     for k in range(i,n):
        #         if k > i and nums[k] == nums[k-1]:
        #             continue  
        #         else:
        #             backtrack2(k+1,n,path+[nums[k]])
                    
        # backtrack2(0,n,[])
        
        
        def backtrack3(i,path):
            path = path[:]
            res.append(path)
            
            for k in range(i,n):
                if k > i and nums[k] == nums[k-1]:
                    continue
                path.append(nums[k])
                backtrack3(k+1,path)
                path.pop()
            backtrack3(0,[])
        return res 
# @lc code=end

