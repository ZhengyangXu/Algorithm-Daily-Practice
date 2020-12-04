#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (38.19%)
# Likes:    2693
# Dislikes: 0
# Total Accepted:    202.4K
# Total Submissions: 529.9K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getk(A,B,k):
            if len(A) == 0:
                return B[k-1]
            if len(B) == 0:
                return A[k-1]
            if k == 1:
                return min(A[0],B[0])
            
            a = A[k//2-1] if len(A)>=k//2 else None  
            b = B[k//2-1] if len(B)>=k//2 else None   
            
            if b is None or (a is not None and a < b):
                return getk(A[k//2:],B,k-k//2)
            else:
                return getk(A,B[k//2:],k-k//2)
        m,n = len(nums1),len(nums2)
        total = m + n  
        if total % 2 == 1:
            return getk(nums1,nums2,(total+1)//2)
        else:
            return (getk(nums1,nums2,(total//2)+1)+getk(nums1,nums2,(total//2)))/2 
    
        
# @lc code=end
        # def getk(k):
        #     index1,index2 = 0,0 
        #     while True:
        #         if index1 == m:
        #             return nums2[index1+k-1]
        #         if index2 == n:
        #             return nums1[index2+k-1]
        #         if k == 1:
        #             return min(nums1[index1],nums2[index2])
                
        #         newindex1 = min(index1 + k // 2 - 1,m-1) 
        #         newindex2 = min(index2 + k // 2 - 1,n-1) 
                
        #         pivot1,pivot2 = nums1[newindex1],nums1[newindex2]
        #         if pivot1 <= pivot2:
        #             k -= newindex1 - index1 + 1 
        #             index1 = newindex1 + 1 
        #         else:
        #             k -= newindex2 - index2 + 1 
        #             index2 = newindex2 + 1 
        # m,n = len(nums1),len(nums2)
        # total = m + n  
        # if total % 2 == 1:
        #     return getk((total+1)//2)
        # else:
        #     return (getk(total//2)+getk(total//2+1))/2  
