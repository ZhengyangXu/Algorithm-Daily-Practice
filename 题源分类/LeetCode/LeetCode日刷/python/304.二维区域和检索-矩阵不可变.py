#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#
# https://leetcode-cn.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (47.27%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    36.9K
# Total Submissions: 70.3K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
#   '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
# 
# 
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
# 
# 
# 
# 示例：
# 
# 
# 给定 matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# 
# 
# 
# 
# 提示：
# 
# 
# 你可以假设矩阵不可变。
# 会多次调用 sumRegion 方法。
# 你可以假设 row1 ≤ row2 且 col1 ≤ col2 。
# 
# 
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):##二维前缀和
        if not matrix or not matrix[0]:
            m,n = 0,0
        else:
            m,n = len(matrix),len(matrix[0])
        self.presum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.presum[i][j+1] = self.presum[i][j] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0 
        for i in range(row1,row2+1):
            ans += self.presum[i][col2+1] - self.presum[i][col1] 
        #total = sum(self.presum[i][col2+1]-self.presum[i][col1] for i in range(row1,row2+1) )
        return ans 
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix


#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         ans = 0
#         row,col = len(self.matrix),len(self.matrix[0])
#         i,j = row1,col1
#         while i <= row2 and i <= row:
#             ans += sum(self.matrix[i][col1:col2+1])
#             i += 1 
            
#         return ans 


#  def __init__(self, matrix: List[List[int]]):##二维前缀和
#         if not matrix or not matrix[0]:
#             m,n = 0,0
#         else:
#             m,n = len(matrix),len(matrix[0])
#         self.presum = [[0]*(n+1) for _ in range(m+1)]
#         for i in range(m):
#             for j in range(n):
#                 self.presum[i+1][j+1] = self.presum[i][j+1]+self.presum[i+1][j]-self.presum[i][j]+matrix[i][j]


#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         return self.presum[row2+1][col2+1]-self.presum[row2+1][col1] - self.presum[row1][col2+1]+self.presum[row1][col1]
