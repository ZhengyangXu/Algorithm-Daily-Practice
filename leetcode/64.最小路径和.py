#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (65.80%)
# Likes:    504
# Dislikes: 0
# Total Accepted:    97.5K
# Total Submissions: 147.9K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = grid[:][:]

        for i in range(1,n):
            dp[0][i] += grid[0][i-1]
        for j in range(1,m):
            dp[j][0] += grid[j-1][0]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= min(grid[i][j]+dp[i-1][j],grid[i][j]+dp[i][j-1])
        return dp[-1][-1]
                
                
            
                

# @lc code=end
#DP
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     for j in range(1,n):
    #         grid[0][j] += grid[0][j-1]
    #     for i in range(1,m):
    #         grid[i][0] += grid[i-1][0]
    #         for j in range(1,n):
    #             grid[i][j] += min(grid[i-1][j],grid[i][j-1])
    #     return grid[-1][-1]

