#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (45.54%)
# Likes:    773
# Dislikes: 0
# Total Accepted:    109.3K
# Total Submissions: 238.4K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
# 示例 1：
#
#
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
#
#
# 示例 2：
#
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#
#
# 示例 3：
#
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1
# matrix[i][j] 为 '0' 或 '1'
#
#
#


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0]*n
        prev = 0  
        maxside = 0
        for i in range(m):
            for j in range(n):
                cur = dp[j]
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[j] = 1 
                    else:
                        dp[j] = min(dp[j-1],dp[j],prev)
                    
                    maxside = max(maxside,dp[j])
                prev = cur 
        
        return maxside*maxside 
                


# @lc code=end

    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     if not matrix:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #     dp = [[0] * (n) for _ in range(m)]
    #     maxside = ·p·
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == '1':
    #                 if i == 0 or j == 0:
    #                     dp[i][j] = 1
    #                 else:
    #                     dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1],
    #                                    dp[i][j - 1]) + 1
    #                 maxside = max(maxside, dp[i][j])
    #     return maxside * maxside