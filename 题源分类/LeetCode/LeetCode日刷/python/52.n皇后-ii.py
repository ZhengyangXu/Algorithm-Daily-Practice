#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# https://leetcode-cn.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (82.18%)
# Likes:    213
# Dislikes: 0
# Total Accepted:    51.5K
# Total Submissions: 62.7K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
# 
# 示例:
# 
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
# [".Q..",  // 解法 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // 解法 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
# 
# 
# 提示：
# 
# 
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或
# N-1 步，可进可退。（引用自 百度百科 - 皇后 ）
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        
        res = 0 
        cols,pos,neg = set(),set(),set()
        
        def dfs(row):
            nonlocal res 
            if row == n:
                res += 1 
                return 
            for col in range(n):
                if col not in cols and row - col not in pos and row + col not in neg:
                    cols.add(col)
                    pos.add(row-col)
                    neg.add(row+col)
                    dfs(row+1)
                    cols.remove(col)
                    pos.remove(row-col)
                    neg.remove(row+col)
            
        dfs(0)
        return res         
        

                
            
# @lc code=end
#   def totalNQueens(self, n: int) -> int:
        
#         res = 0 
#         board = [["."] * n for _ in range(n)]
        
#         def isValid(row,col):
            
#             for i in range(row):
#                 if board[i][col] == "Q":
#                     return False 
#             i,j = row-1,col-1
            
#             while i >= 0 and j >= 0:
#                 if board[i][j] == "Q":
#                     return False  
#                 i -= 1 
#                 j -= 1 
                
#             p,q = row-1,col+1 
#             while p >= 0 and q < n:
#                 if board[p][q] == "Q":
#                     return False  
#                 p -= 1 
#                 q += 1 
            
#             return True 
        
#         def dfs(row):
#             nonlocal res 
#             if row == n:
#                 res += 1 
                
#             for col in range(n):
#                 if not isValid(row,col):
#                     continue 
#                 board[row][col] = "Q"
#                 dfs(row + 1)
#                 board[row][col] = "."
                
                
#         dfs(0)
#         return res 
