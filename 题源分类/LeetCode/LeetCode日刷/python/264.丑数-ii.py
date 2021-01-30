#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (55.05%)
# Likes:    453
# Dislikes: 0
# Total Accepted:    42.5K
# Total Submissions: 77.2K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
# 
# 丑数就是质因数只包含 2, 3, 5 的正整数。
# 
# 示例:
# 
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 
# 说明:  
# 
# 
# 1 是丑数。
# n 不超过1690。
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        res = 0  
        for _ in range(n):
            res = heapq.heappop(heap)
            # while heap and res == heap[0]:
            #     res = heapq.heappop(heap)
            a,b,c = res*2,res*3,res*5
            for t in [a,b,c]:
                if t not in heap:
                    heapq.heappush(heap,t)
        return res
                
        
 
# @lc code=end

    # def nthUglyNumber(self, n: int) -> int:
        
    #     if n < 7: 
    #         return n   
    #     res = [1,2,3,4,5,6]
    #     t2,t3,t5 = 3,2,1  
        
    #     for i in range(6,n):
    #         res.append(min(res[t2]*2,min(res[t3]*3,res[t5]*5)))
    #         while res[t2]*2 <= res[i]:
    #             t2 += 1 
    #         while res[t3]*3 <= res[i]:
    #             t3 += 1 
    #         while res[t5]*5 <= res[i]:
    #             t5 += 1 
    #     return res[-1]