#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (60.25%)
# Likes:    878
# Dislikes: 0
# Total Accepted:    138.4K
# Total Submissions: 228.5K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11
# 不是。
#
#
#
# 示例 1：
#
#
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
#
# 示例 2：
#
#
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
#
#
# 提示：
#
#
# 1
#
#
#

# @lc code=start
class Solution:

    def numSquares(self, n: int) -> int:
        if not n:
            return 0 
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0 
        for i in range(1,n+1):
            for j in range(1,int(sqrt(i))+1):
                dp[i] = min(dp[i],dp[i-j*j] + 1)
        return dp[n]
          


# @lc code=end

    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(0, int(sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)

        dp[0] = 0
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]
    
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        
        for i in range(1,n+1):
            dp[i] = i 
            for j in range(1,int(sqrt(i))+1):
                dp[i] = min(dp[i],dp[i-j*j]+1)
        return dp[n]
    
    
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        
        for i in range(1,n+1):
            minn = float('inf')
            for j in range(1,int(sqrt(i))+1):
                minn = min(minn,dp[i-j*j])
            dp[i] = minn + 1 
        return dp[n]
    
     def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0 
        for i in range(1,int(sqrt(n))+1):
            t = i * i 
            for j in range(t,n+1):
                dp[j] = min(dp[j],dp[j-t]+1)
                
        return dp[n]
    
    
class node:
    def __init__(self,value,step=0):
        self.value = value
        self.step = step
    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value,self.step)
class Solution:



    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])
        
        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - n*n for n in range(1,int(vertex.value**.5)+1)]
            for i in residuals:
                new_vertex = node(i, vertex.step+1)
                if i==0:                   
                    return new_vertex.step
                    
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
                                        
        return -1
