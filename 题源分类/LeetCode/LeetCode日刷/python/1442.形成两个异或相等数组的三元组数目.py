#
# @lc app=leetcode.cn id=1442 lang=python3
#
# [1442] 形成两个异或相等数组的三元组数目
#
# https://leetcode-cn.com/problems/count-tri+plets-that-can-form-two-arrays-of-equal-xor/description/
#
# algorithms
# Medium (67.40%)
# Likes:    122
# Dislikes: 0
# Total Accepted:    22.1K
# Total Submissions: 28.1K
# Testcase Example:  '[2,3,1,6,7]'
#
# 给你一个整数数组 arr 。
# 
# 现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。
# 
# a 和 b 定义如下：
# 
# 
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# 
# 
# 注意：^ 表示 按位异或 操作。
# 
# 请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [2,3,1,6,7]
# 输出：4
# 解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
# 
# 
# 示例 2：
# 
# 输入：arr = [1,1,1,1,1]
# 输出：10
# 
# 
# 示例 3：
# 
# 输入：arr = [2,3]
# 输出：0
# 
# 
# 示例 4：
# 
# 输入：arr = [1,3,5,7,9]
# 输出：3
# 
# 
# 示例 5：
# 
# 输入：arr = [7,11,12,9,5,2,7,17,22]
# 输出：8
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 300
# 1 <= arr[i] <= 10^8
# 
# 
#

# @lc code=start
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        from collections import Counter
        cnt,total = Counter(),Counter() 
        s = count = 0
        n = len(arr)
        for k,val in enumerate(arr):
            t = s ^ val
            if t in cnt:
                count += cnt[t]*k - total[t]
            cnt[s] += 1 
            total[s] += k 
            s = t 
                
                
        
            
            
        return count
                        
            
        

        
# @lc code=end

    # def countTriplets(self, arr: List[int]) -> int:
    #     from collections import Counter
    #     s = [0]
    #     for i in range(len(arr)):
    #         s.append(s[-1]^arr[i])
    #     count = 0
    #     n = len(arr)
    #     # for i in range(n):
    #     #     for j in range(i+1,n):
    #     #         for k in range(j,n):
    #     #             if s[i] == s[k+1]:
    #     #                 count += 1 
    #     # for i in range(n):
    #     #     for k in range(i+1,n):
    #     #         if s[i] == s[k+1]:
    #     #             count += k - i 
    #     # cnt,total = Counter(),Counter() 
    #     # for k in range(n):
    #     #     if s[k+1] in cnt:
    #     #         count +=  cnt[s[k+1]] * k - total[s[k+1]]
            
    #     #     cnt[s[k]] += 1 
    #     #     total[s[k]] += k
        
        
            
            
    #     return count 