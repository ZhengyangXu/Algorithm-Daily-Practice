#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (41.60%)
# Likes:    559
# Dislikes: 0
# Total Accepted:    93K
# Total Submissions: 223K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 
# 示例 1:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2:
# 
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rstart,rend,cstart,cend = 0,len(matrix)-1,0,len(matrix[0])-1
        res = []
        while rstart <= rend and cstart <= cend:
            for i in range(cend+1):
                res.append(matrix[rstart][i])
                
            for j in range(rstart+1,rend+1):
                res.append(matrix[j][cend])
                
            if rstart < rend and cstart < cend:
                for i in range(rend-1,rstart,-1):
                    res.append(matrix[i][cstart])
                    
                for i in range()
       
                
        
        
# @lc code=end

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix:
#             return []
#         rstart,rend,cstart,cend = 0,len(matrix),0,len(matrix[0])
#         res = []
#         i,j = 0,0
#         while rstart <= i < rend and cstart <= j < cend:
#             while i == rstart and j < cend :
#                 res.append(matrix[i][j])
#                 j += 1 
#             rstart += 1   
#             i += 1
#             j -= 1
               
#             while j == cend-1 and i < rend:
#                 res.append(matrix[i][j]) 
#                 i += 1
#             cend -= 1 
#             j -= 1
#             i -= 1
                
#             while i == rend - 1 and j >= cstart:
#                 res.append(matrix[i][j])
#                 j -= 1 
#             rend -= 1 
#             i -= 1
#             j += 1
            
#             while j == cstart and i >= rstart:
#                 res.append(matrix[i][j])
#                 i -= 1 
#             cstart += 1 
#             j += 1
#             i += 1
#         return res[0:len(matrix)*len(matrix[0])]    