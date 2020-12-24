#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Hard (51.71%)
# Likes:    450
# Dislikes: 0
# Total Accepted:    69.3K
# Total Submissions: 134K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3, k = 3
# 输出："213"
# 
# 
# 示例 2：
# 
# 
# 输入：n = 4, k = 9
# 输出："2314"
# 
# 
# 示例 3：
# 
# 
# 输入：n = 3, k = 1
# 输出："123"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start

    # def getPermutation(self, n: int, k: int) -> str:
    #     def backtrack(n,k,index,path):
    #         if index == n:
    #             return 
            
    #         cnt = factorial[n-1-index]
    #         for i in range(1,n+1):
    #             if used[i]:
    #                 continue  
    #             if cnt < k:
    #                 k -= cnt  
    #                 continue  
    #             path.append(str(i))
    #             used[i] = True
    #             backtrack(n,k,index+1,path)
    #             return  
            
    #     if n == 0:
    #         return ""
        
    #     used=[0]*(n+1)
    #     path = []
    #     factorial = [1]*(n+1)
    #     for i in range(2,n+1):
    #         factorial[i] = factorial[i-1]*i
            
    #     backtrack(n,k,0,path)
    #     return "".join(path)
            
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1,n):
            factorial.append(factorial[-1]*i)
            
        k -= 1 
        used = [0]*(n+1)
        ans = []
        
        for i in range(1,n+1):
            order = k // factorial[n-i] + 1 
            for j in range(1,n+1):
                if used[j] != 0:
                    continue  
                order -= 1  
                if order == 0:
                    ans.append(str(j))
                    used[j] = 1  
                    break  
            k %= factorial[n-i]
        
        return "".join(ans) 
        

            
    