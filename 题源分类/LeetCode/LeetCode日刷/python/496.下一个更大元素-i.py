#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#
# https://leetcode-cn.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (65.80%)
# Likes:    288
# Dislikes: 0
# Total Accepted:    48.7K
# Total Submissions: 74K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# 给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2
# 中的下一个比其大的值。
# 
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
# 
# 
# 
# 示例 1:
# 
# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
# ⁠   对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
# ⁠   对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
# ⁠   对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
# 
# 示例 2:
# 
# 输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
# 对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
# ⁠   对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
# 
# 
# 
# 
# 提示：
# 
# 
# nums1和nums2中所有元素是唯一的。
# nums1和nums2 的数组大小都不超过1000。
# 
# 
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:## 从左到右入栈
        
        dic,stack = {},[]
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] <= nums2[i]:
                dic[nums2[stack.pop()]] = nums2[i]
                
            stack.append(i)
            
        return [dic.get(num1,-1) for num1 in nums1]
                
            

 
# @lc code=end
#  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:## 暴力解法
#         dic = dict()
#         res = []
        
#         for i in range(len(nums2)):
#             j = i + 1 
#             while j < len(nums2) and nums2[j] <= nums2[i]:
#                 j += 1 
            
#             if j < len(nums2) and nums2[j] > nums2[i]:
#                 dic[nums2[i]] = nums2[j]
                
#         for num1 in nums1:
#             res.append(dic[num1] if num1 in dic else -1)
#         return res 
        
            


        # return res  
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:## 暴力解法
    #     dic = dict()

        
    #     for i in range(len(nums2)):
    #         for j in range(i+1,len(nums2)):
    #             if nums2[j] > nums2[i]:
    #                 dic[nums2[i]] = nums2[j]
    #                 break  
    #     res = [dic.get(num1,-1) for num1 in nums1]
        
    #     return res 
    
    
    
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:## 倒入单调栈法
        # dic,stack = {},[]
        # for i in range(len(nums2)-1,-1,-1):
        #     while stack and nums2[stack[-1]] <= nums2[i]:
        #         stack.pop() 
        #     if stack:
        #         dic[nums2[i]] = nums2[stack[-1]]
        #     stack.append(i) 
        
        # return [dic.get(num,-1) for num in nums1]
        
        #思路:单调栈法用于左边或右边第一个比自己大或比自己小的数的寻找。找右边第一个比自己大的数，数组从
        # 右向左倒入栈，保证栈顶到栈底是不单增的，因为栈底是最接近于右边的数的位置，如果新入栈的数大于
        #栈顶的数，那pop()栈。这样可以保证整个栈是递减的