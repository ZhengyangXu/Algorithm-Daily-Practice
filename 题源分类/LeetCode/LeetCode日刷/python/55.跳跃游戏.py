#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (41.36%)
# Likes:    959
# Dislikes: 0
# Total Accepted:    176.4K
# Total Submissions: 426K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个位置。
# 
# 示例 1:
# 
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 
# 
# 示例 2:
# 
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool: ##暴力解法 双重循环 超时
        if len(nums) == 1:
            return True 
        n = len(nums)
        dp = [False for _ in range(n)]
        
        dp[0] = True 
        for i in range(n):
            for j in range(1,nums[i]+1):
                if i + j < n and dp[i]:
                    dp[i+j] = True 
                if not dp[i]:
                    return False  
                    break 
  
        return dp[-1]
                
        
                
# @lc code=end
# class Solution:
#     def canJump(self, nums: List[int]) -> bool: ##暴力解法 双重循环 超时
#         if len(nums) == 1:
#             return True 
#         dp = [False for _ in range(len(nums))]
#         dp[0] = True
#         for i in range(len(nums)):
#             for j in range(1,nums[i]+1):
#                 if i + j < len(nums) and dp[i]:
#                     dp[i+j] = True
                
#         return dp[-1]
    # def canJump(self, nums: List[int]) -> bool: ##暴力解法 双重循环 超时
    #     if len(nums) == 1:
    #         return True 
    #     last = len(nums)
    #     maxi = 0 
    #     for i in range(last):
    #         if i <= maxi:
    #             maxi = max(maxi,i+nums[i])
    #             if maxi >= last-1:
    #                 return True
                
            
                
    # #     return False  
    
    
    #     def canJump(self, nums: List[int]) -> bool: ##暴力解法 双重循环 超时
    #     if len(nums) == 1:
    #         return True 
        
    #     maxi = 0 
    #     for i in range(len(nums)):
    #         if i > maxi:
    #             return False 
    #         maxi = max(maxi,i+nums[i])
    #     return True 
    
    
        # def canJump(self, nums: List[int]) -> bool: ##暴力解法 双重循环 超时
        # if len(nums) == 1:
        #     return True 
        # dp = [False for _ in range(len(nums))]
        # dp[0] = True
        # for i in range(1,len(nums)):
        #     for j in range(i):
        #         if nums[j] + j >= i and dp[j]:
        #             dp[i] = True
        #             break 
        # return dp[-1]