#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (52.86%)
# Likes:    691
# Dislikes: 0
# Total Accepted:    99.6K
# Total Submissions: 188.2K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 
# 
# 
# 进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
# 示例 2：
# 
# 
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = dict()
        long = 0 
        for num in nums:
            if num not in dic:
                left = dic.get(num-1,0) 
                right = dic.get(num+1,0)
                cur = 1 + left + right 
                if cur > long:
                    long = cur  
                    
                dic[num] = cur  
                dic[num-left] = cur  
                dic[num+right] = cur 
        
        return long 
            
        
# @lc code=end

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     numset = set(nums)
    #     long = 0 
    #     for num in numset:
    #         if num-1 not in numset:
    #             curnum = num  
    #             cur = 1 
    #             while curnum + 1 in numset:
    #                 cur += 1 
    #                 curnum += 1 
    #             long = max(cur,long)
    #     return long 