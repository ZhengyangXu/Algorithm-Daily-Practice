#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
# https://leetcode-cn.com/problems/transpose-matrix/description/
#
# algorithms
# Easy (68.31%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    64.1K
# Total Submissions: 93.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
# 
# 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]
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
# 1 
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]: ## 直接用zip转置，然后再换成list
        import numpy as np 
        return np.transpose(matrix).tolist()
# @lc code=end

    # def transpose(self, matrix: List[List[int]]) -> List[List[int]]: ## 按照题意转置
        
    #     row = len(matrix)
        
    #     col = len(matrix[0])
        
    #     res = [[0]*row for _ in range(col)]
        
    #     for i in range(col):
    #         for j in range(row):
    #             res[i][j] = matrix[j][i]
                
    #     return res 
    
    
    
    # def transpose(self, matrix: List[List[int]]) -> List[List[int]]: ## 直接用zip转置，然后再换成list
    #     tmatrix = list(zip(*matrix))
        
    #     row,col = len(tmatrix),len(matrix[0])
    #     res = []
    #     for i in range(row):
    #         res.append(list(tmatrix[i]))
    #     return res 