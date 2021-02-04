#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (71.87%)
# Likes:    1147
# Dislikes: 0
# Total Accepted:    203K
# Total Submissions: 282.1K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1：
# 
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2：
# 
# 输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
# 
# 提示：
# 
# 
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都是独一无二的。
# 1 <= target <= 500
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()    
        def backtrack(candidates,path,target):
            if target < 0:
                return  
            if target == 0:
                res.append(path)
            
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break 
                backtrack(candidates[i:],path+[candidates[i]],target-candidates[i])
                
        backtrack(candidates,[],target)
        
        return res  
            
# @lc code=end

    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     res = []
        
    #     def backtrack(candidates,path,target):
    #         if target < 0:
    #             return  
    #         if target == 0:
    #             path.sort()
    #             if path not in res:
    #                res.append(path)
                
    #         for i in candidates:
    #             backtrack(candidates,path+[i],target-i)
                
    #     backtrack(candidates,[],target)
        
    #     return res  