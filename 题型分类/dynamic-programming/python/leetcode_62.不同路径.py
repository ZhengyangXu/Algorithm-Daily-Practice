#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (60.71%)
# Likes:    600
# Dislikes: 0
# Total Accepted:    120.2K
# Total Submissions: 196.9K
# Testcase Example:  '3\n2'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 问总共有多少条不同的路径？
# 
# 
# 
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
# 
# 
# 
# 示例 1:
# 
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 
# 
# 示例 2:
# 
# 输入: m = 7, n = 3
# 输出: 28
# 
# 
# 
# 提示：
# 
# 
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10 ^ 9
# 
# 
#
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         ## 普通dp
#         # if not m or not n:
#         #     return 0 
#         # if m == 1 or n == 1:
#         #     return 1 
#         # dp = [[1]*n] + [[1]+[0]*(n-1)]*(m-1)
        
#         # for i in range(1,m):
#         #     for j in range(1,n):
#         #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
#         # return dp[m-1][n-1]
        
    #     class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:

        
    #     ##O(n)空间DP
        
    #     if not m or not n:
    #         return 0 
    #     if m == 1 or n == 1:
    #         return 1 
    #     pre = [1]*n  
    #     cur = [1]*n 
        
    #     for i in range(1,m):
    #         for j in range(1,n):
    #             cur[j] = cur[j-1]+pre[j]
    #         pre = cur[:]
    #     return pre[-1]
    
        # def uniquePaths(self, m: int, n: int) -> int:

        
        # ##O(n)空间DP
        
        # if not m or not n:
        #     return 0 
        # if m == 1 or n == 1:
        #     return 1 
        # cur = [1] * n  
        # for i in range(1,m):
        #     for j in range(1,n):
        #         cur[j] += cur[j-1]
        # return cur[-1]
        
    #     class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:##递归+memo
    #     memo = {}
    #     res = 0
    #     def dfs(i,j):
            
    #         if (i,j) in memo:
    #             return memo[(i,j)]
    #         if i > m-1 or j > n-1:
    #             return 0
            
    #         if i == m-1 and j == n-1:
    #             return 1  
            
    #         res = dfs(i+1,j) + dfs(i,j+1)
    #         memo[(i,j)] = res  
    #         return res  

    #     return dfs(0,0)
    
    
        # def uniquePaths(self, m: int, n: int) -> int:##递归+memo
        # memo = {}
        # def dfs(i,j):
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if i == 0 or j == 0:
        #         return 1
            
        #     if i < 0 or j < 0:
        #         return 0  
            
        #     res = dfs(i-1,j) + dfs(i,j-1)
        #     memo[(i,j)] = res 
        #     return res  
        # return dfs(m-1,n-1)
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:##递归+memo
        
        return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))
            
            
                    