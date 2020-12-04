#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (42.25%)
# Likes:    426
# Dislikes: 0
# Total Accepted:    80K
# Total Submissions: 189.5K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 
# 示例:
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 运行你的函数后，矩阵变为：
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 解释:
# 
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None: ## DFS
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return  
        
        f = {}
        def find(x):
            f.setdefault(x,x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        def union(x,y):
            f[find(y)] = find(x)
            
        if not board:
            return  
        
        m,n = len(board),len(board[0])
        
        dummy = m*n
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if i in (0,m-1) or j in (0,n-1):
                        union(i*n+j,dummy)
                    else:
                        for x,y in ((-1,0),(1,0),(0,1),(0,-1)):
                            if board[i+x][j+y] == "O":
                                union(i*n+j,(i+x)*n+(j+y))
        
        for i in range(m):
            for j in range(n):
                if find(dummy) == find(i*n+j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
                    
        

# @lc code=end

        
        # for row in range(len(board)):
        #     for col in range(len(board[0])):
        #         if board[row][col] == "X":
        #             continue  
        #         else:
        #             if row == 0 or row == len(board) or col == 0 or col == len(board[0]):
        #                 continue 
        #             else:
        #                 if "X" in board[row][0:col] and "X" in board[row][col+1:]:
        #                     for i in range(0,row):
        #                         for j in range(row+1,len(board)):
        #                             if board[i][col] == "X" and board[j][col] == "X":
        #                                 board[row][col] = "X"
        # return board 
        
        
        ##错误：三个互相连通也是连通
        
        
        
        #  def solve(self, board: List[List[str]]) -> None:
        # """
        # Do not return anything, modify board in-place instead.
        # """
        # if not board:
        #     return 
        # m,n = len(board),len(board[0])
        # queue = []
        
        # for i in range(m):
        #     for j in (0,n-1):
        #         if board[i][j] == "O":
        #             queue.append((i,j))
                    
        # for j in range(1,n-1):
        #     for i in (0,m-1):
        #         if board[i][j] == "O":
        #             queue.append((i,j))
                    
        # while queue:
        #     x,y = queue.pop(0)
        #     board[x][y] = "B"
        #     for mx,my in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        #         if 0 <= mx < m and 0 <= my < n and board[mx][my] == "O":
        #             queue.append((mx,my))
                    
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == "B":
        #             board[i][j] = "O"
        #         elif board[i][j] == "O":
        #             board[i][j] = "X"
                                    
        # return board 
        
        
        #     def solve(self, board: List[List[str]]) -> None: ## DFS
        # """
        # Do not return anything, modify board in-place instead.
        # """
        # if not board:
        #     return 
        # m,n = len(board),len(board[0])
        
        # def dfs(i,j):
        #     board[i][j] = "B"
        #     for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
        #         if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
        #             dfs(x,y)
                    
        # edge = []           
        # for i in range(m):
        #     for j in (0,n-1):
        #         if board[i][j] == "O":
        #             edge.append((i,j))
                    
        # for j in range(1,n-1):
        #     for i in (0,m-1):
        #         if board[i][j] == "O":
        #             edge.append((i,j))          
        
        # for i,j in edge:
        #     dfs(i,j)  
        
                    
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == "B":
        #             board[i][j] = "O"
        #         elif board[i][j] == "O":
        #             board[i][j] = "X"
                                    
        # return board 