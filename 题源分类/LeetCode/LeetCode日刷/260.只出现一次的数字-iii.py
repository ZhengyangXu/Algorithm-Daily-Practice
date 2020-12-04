#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
# https://leetcode-cn.com/problems/single-number-iii/description/
#
# algorithms
# Medium (73.92%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    32.4K
# Total Submissions: 43.8K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
# 
# 示例 :
# 
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
# 
# 注意：
# 
# 
# 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
# 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
# 
# 
#

# @lc code=start
class Solution:
    from collections import Counter
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0 
        for num in nums:
            bitmask ^= num
            
        diff = bitmask & (-bitmask)
        
        x = 0
        for num in nums:
            if num & diff:
                x ^= num  
                
        return [x,bitmask^x]
            
        
# @lc code=end
# from collections import Counter  ## 常规解法 hash set
    # def singleNumber(self, nums: List[int]) -> List[int]:
    #     counter = Counter(nums)
    #     res = []
    #     for key,value in counter.items():
    #         if value != 2:
    #             res.append(key)
                
    #     return res  
    
    
    #     from collections import Counter
    # def singleNumber(self, nums: List[int]) -> List[int]:
    #     res = []
    #     for number in nums:
    #         if number not in res:
    #             res.append(number)
    #         else:
    #             res.remove(number)
    #     return res 