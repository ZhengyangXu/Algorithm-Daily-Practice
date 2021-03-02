#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#
# https://leetcode-cn.com/problems/image-smoother/description/
#
# algorithms
# Easy (55.15%)
# Likes:    70
# Dislikes: 0
# Total Accepted:    13K
# Total Submissions: 23.6K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入)
# ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。
# 
# 示例 1:
# 
# 
# 输入:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# 输出:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
# 
# 
# 注意:
# 
# 
# 给定矩阵中的整数范围为 [0, 255]。
# 矩阵的长和宽的范围均为 [1, 150]。
# 
# 
#

# @lc code=start
class Solution:
    import math
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        
        row = len(M)
        col = len(M[0])
        
        for r in M:
            r.insert(0,0)
            r.append(0)
            
        zeros = [0 for _ in range(col + 2)]
        M.insert(0,zeros)
        M.append(zeros)

        res = [[0]*col for _ in range(row)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                s = M[i][j]
                for d in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    x,y = d
                    s += M[i+x][j+y]
                avg = math.floor(s/8) 
                res[i-1][j-1] = avg  
        return res 
                    
                 
        
# @lc code=end

