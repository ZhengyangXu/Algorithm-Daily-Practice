#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (45.56%)
# Likes:    171
# Dislikes: 0
# Total Accepted:    53.2K
# Total Submissions: 116.8K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
# 
# 
# 
# 示例：
# 
# 
# 输入：[1,12,-5,-6,50,3], k = 4
# 输出：12.75
# 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# 
# 提示：
# 
# 
# 1 k n 
# 所给数据范围 [-10,000，10,000]。
# 
# 
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:## 滑动窗口
        
        n = len(nums)
        presum = [0]*(n+1)
        
        for i in range(n):
            presum[i+1] = presum[i] + nums[i]
        maxAvg = -float('inf')
        for i in range(k-1,n):
            maxAvg = max(maxAvg,presum[i+1]-presum[i+1-k])
            
        return maxAvg/k
            

        
# @lc code=end

    # def findMaxAverage(self, nums: List[int], k: int) -> float:## 暴力解 超时
        
    #     maxtotal = -float('inf')
    #     index = 0
    #     for i in range((len(nums)-k)+1):
    #         if maxtotal < sum(nums[i:i+k]):
    #             maxtotal = sum(nums[i:i+k])
    #             index = i 
                
    #     return maxtotal/k
    
    # def findMaxAverage(self, nums: List[int], k: int) -> float:## 滑动窗口
        
    #     total=maxtotal = sum(nums[:k])

    #     for i in range(k,len(nums)):
    #         total = total + nums[i] - nums[i-k]
    #         maxtotal = max(maxtotal,total)
                
    #     return maxtotal/k