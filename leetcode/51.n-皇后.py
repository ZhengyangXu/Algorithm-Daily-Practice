#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (73.36%)
# Likes:    676
# Dislikes: 0
# Total Accepted:    89.5K
# Total Submissions: 122K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 
# 
# 示例：
# 
# 输入：4
# 输出：[
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
# 
# 
# 提示：
# 
# 
# 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
# 
# 
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        if n == 0:
            return res  
        
        col,main,sub = 0,0,0 
        path = []
        
        def dfs(row,col,sub,main,path):
            if row == n:
                board = convert2board(path)
                res.add(board)
                return  
            
            for i in range(n):
                if ((col >> i) & 1) == 0 and ((main >> (row-i+n-1)) & 1) == 0 and ((sub >> (row+i)) & 1) == 0:
                    path.append(i)
                    col ^= (1<<i)
                    main ^= (1<<(row-i+n-1))
                    sub ^= (1<<(row+i))
                    
                    dfs(row+1,col,sub,main,path)
                    
                    sub ^= (1 << (row+i))
                    main ^= (1<<(row-i+n-1))
                    col ^= (1<<i)
                    path.pop()
        def convert2board(path):
            board = []
            for i in path:
                row = []
                row.append(".")
                    
  
        
            
        
# @lc code=end

    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     board = [["." for _ in range(n)] for _ in range(n)]
    #     res = []
        
    #     def isValid(board,row,col):
            
    #         for i in range(row):
    #             if board[i][col] == "Q":
    #                 return False 
            
    #         i,j = row-1,col-1 
    #         while i >= 0 and j >= 0:
    #             if board[i][j] == "Q":
    #                 return False
    #             i -= 1
    #             j -= 1 
    #         i,j = row-1,col+1
    #         while i >= 0 and j < n:
    #             if board[i][j] == "Q":
    #                 return False
    #             i -= 1 
    #             j += 1 
    #         return True
        
    #     def backtrack(board,row):
            
    #         if row == len(board):
    #             res.append(["".join(board[i]) for i in range(row)])
    #             return  
            
    #         for col in range(len(board[0])):
    #             if not isValid(board,row,col):
    #                 continue  
    #             board[row][col] = "Q"
    #             backtrack(board,row+1)
    #             board[row][col] = "."
        
    #     backtrack(board,0)
        
    #     return res 
        