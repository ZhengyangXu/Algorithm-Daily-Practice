#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (66.67%)
# Likes:    691
# Dislikes: 0
# Total Accepted:    61.7K
# Total Submissions: 92.6K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过填充空格来解决数独问题。
# 
# 一个数独的解法需遵循如下规则：
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 
# 
# 空白格用 '.' 表示。
# 
# 
# 
# 一个数独。
# 
# 
# 
# 答案被标成红色。
# 
# 提示：
# 
# 
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
# 
# 
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0]*9
        cols = [0]*9
        cells = [[0]*3 for _ in range(3)]
        tofill = []
        valid = False 
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    tofill.append((i,j))
                else:
                    num = int(board[i][j]) -1 
                    rows[i] ^=  (1<<num)  
                    cols[j] ^= (1<<num)  
                    rows[i//3][j//3] ^= (1<<num)  
                    
        def backtrack(pos):
            nonlocal valid
            if pos == len(tofill):
                valid = True  
                return  
            
            row,col = tofill[pos]
            
            for num in range(9):
                if rows[row] >> num & 1 == cols[col] >> num & 1 == cells[row//3][col//3] >> num & 1 == 0:
                    rows[row] = rows[row] | (1<<num)  
                    cols[col] = rows[col] | (1<<num)  
                    rows[row//3][col//3] = cells[row//3][col//3] | (1<<num) 
                    board[row][col] = str(num + 1)
                    backtrack(pos+1)
                    rows[row] >> num = 1  
                if valid:
                    return  
                
        backtrack(0)
                    


                     
            

# @lc code=end


    # def solveSudoku(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     def isValid(board,r,c,n):
    #         if not board:
    #             return False   
            
    #         for i in range(9):
    #             if board[r][i] == n or board[i][c] == n or board[(r//3)*3+i//3][(c//3)*3+i%3] == n:
    #                 return False 
    #         return True 
        
    #     def backtrack(board,r,c):
            
    #         if c == 9:
    #             return backtrack(board,r+1,0)
            
    #         if r == 9:
    #             return True
            
    #         for i in range(r,9):
    #             for j in range(c,9):
    #                 if board[i][j] != ".":
    #                     return backtrack(board,i,j+1)
                    
    #                 for num in range(1,10):
    #                     if not isValid(board,i,j,str(num)):
    #                         continue 
    #                     board[i][j] = str(num)
    #                     if backtrack(board,i,j+1):
    #                         return True 
    #                     board[i][j] = '.'
    #                 return False 
    #     backtrack(board,0,0)
    
    
    
        # def solveSudoku(self, board: List[List[str]]) -> None:
        # """
        # Do not return anything, modify board in-place instead.
        # """
        # rows = [[0]*9 for _ in range(9)]
        # cols = [[0]*9 for _ in range(9)]
        # cells = [[[0]*9 for _ in range(3)] for _ in range(3)]
        # tofill = []
        # valid = False 
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] == ".":
        #             tofill.append((i,j))
        #         else:
        #             num = int(board[i][j]) -1 
        #             rows[i][num] = cols[j][num] = cells[i//3][j//3][num] = True  
                    
        # def backtrack(pos):
        #     nonlocal valid
        #     if pos == len(tofill):
        #         valid = True  
        #         return  
            
        #     row,col = tofill[pos]
            
        #     for num in range(9):
        #         if rows[row][num] == cols[col][num] == cells[row//3][col//3][num] == False:
        #             rows[row][num] = cols[col][num] = cells[row//3][col//3][num] = True 
        #             board[row][col] = str(num + 1)
        #             backtrack(pos+1)
        #             rows[row][num] = cols[col][num] = cells[row//3][col//3][num] = False  
        #         if valid:
        #             return  
                
        # backtrack(0)
                    