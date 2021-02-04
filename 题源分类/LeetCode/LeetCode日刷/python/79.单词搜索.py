#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (43.94%)
# Likes:    765
# Dislikes: 0
# Total Accepted:    135.9K
# Total Submissions: 308.5K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
# 
# 
# 
# 提示：
# 
# 
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board:
            return False  
        
        if not word:
            return True  
        
        row,col = len(board),len(board[0])
        
        marked = [[False for _ in range(col)] for _ in range(row)]
        
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        def dfs(i,j,k):
            
            if word[k] != board[i][j]:
                return False  
            
            if k == len(word) - 1:
                return True 
            
            marked[i][j] = True  
            
            res = False  
            for x,y in dirs:
                newi,newj = i+x,j+y  
                
                if 0 <= newi < row and 0 <= newj < col and not marked[newi][newj]:
                    if dfs(newi,newj,k+1):
                        res = True  
                        break 
            marked[i][j] = False    
            return res  
                        
 
        
        for i in range(row):
            for j in range(col):
                    if dfs(i,j,0):
                        return True
                    
        return False
            
        
    

        
   
        
# @lc code=end

    # def exist(self, board: List[List[str]], word: str) -> bool:
        
    #     if not board:
    #         return False  
        
    #     if not word:
    #         return True  
        
    #     row,col = len(board),len(board[0])
        
    #     marked = [[[False] for _ in range(col)] for _ in range(row)]
        
    #     def dfs(i,j,k,marked):
    #         if k == len(word)-1:
    #             return True 
    #         while 0 <= i < row and 0<= j < col:
    #             if board[i][j] == word[k] and not marked[i][j]:
    #                 marked[i][j] = True 
    #                 if i != 0 and j != 0:
    #                     for (x,y) in [(-1,0),(1,0),(0,1),(0,-1)]:
    #                         dfs(i+x,y+j,k+1,marked)
                            
    #                 if i == 0:
    #                     for (x,y) in [(1,0),(0,1),(0,-1)]:
    #                         dfs(i+x,y+j,k+1,marked)
    #                 if j == 0:
    #                     for (x,y) in [(-1,0),(1,0),(0,1),]:
    #                         dfs(i+x,y+j,k+1,marked)
                        
 
        
    #     for i in range(row):
    #         for j in range(col):
    #                 if dfs(i,j,0,marked):
    #                     return True  错误
        
        
        
#    def exist(self, board: List[List[str]], word: str) -> bool:
        
#         if not board:
#             return False  
        
#         if not word:
#             return True  
        
#         row,col = len(board),len(board[0])
        
#         marked = [[False for _ in range(col)] for _ in range(row)]
        
#         dirs = [(0,-1),(0,1),(1,0),(-1,0)]
        
#         def dfs(board,word,k,i,j,marked):
#             if k == len(word)-1:
#                 return board[i][j] == word[k]
            
#             if board[i][j] == word[k]:
#                 marked[i][j] = True  
#                 for x,y in dirs:
#                     newi,newj = i+x,j+y  
                    
#                     if 0 <= newi < row and 0 <= newj < col and not marked[newi][newj] and dfs(board,word,k+1,newi,newj,marked):
#                         return True 
#                 marked[i][j] = False 
#             return False 
        
#         for i in range(row):
#             for j in range(col):
#                 res = dfs(board,word,0,i,j,marked)

#         return res

    # def exist(self, board: List[List[str]], word: str) -> bool:
        
    #     if not board:
    #         return False  
        
    #     if not word:
    #         return True  
        
    #     row,col = len(board),len(board[0])
        
    #     marked = [[False for _ in range(col)] for _ in range(row)]
        
    #     dirs = [(0,-1),(0,1),(1,0),(-1,0)]
        
    #     def dfs(i,j,k):
    #         if board[i][j] != word[k]:
    #             return False  
            
    #         if k == len(word) - 1:
    #             return True 
            
    #         marked[i][j] = True 
            
    #         res = False  
            
    #         for x,y in dirs:
    #             newi,newj = i+x,j+y 
    #             if 0 <= newi < row and 0 <= newj < col:
    #                 if not marked[newi][newj]:
    #                     if dfs(newi,newj,k+1):
    #                         res = True 
    #                         break  
                        
    #         marked[i][j] = False   
    #         return res
        
    #     for i in range(row):
    #         for j in range(col):
    #             if dfs(i,j,0):
    #                 return True  
    #     return False         