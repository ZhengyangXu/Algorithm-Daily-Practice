#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
# https://leetcode-cn.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (61.23%)
# Likes:    444
# Dislikes: 0
# Total Accepted:    105K
# Total Submissions: 171K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 
# 
# 
# 
# 上图是一个部分填充的有效的数独。
# 
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
# 
# 示例 1:
# 
# 输入:
# [
# ⁠ ["5","3",".",".","7",".",".",".","."],
# ⁠ ["6",".",".","1","9","5",".",".","."],
# ⁠ [".","9","8",".",".",".",".","6","."],
# ⁠ ["8",".",".",".","6",".",".",".","3"],
# ⁠ ["4",".",".","8",".","3",".",".","1"],
# ⁠ ["7",".",".",".","2",".",".",".","6"],
# ⁠ [".","6",".",".",".",".","2","8","."],
# ⁠ [".",".",".","4","1","9",".",".","5"],
# ⁠ [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# [
# ["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: false
# 解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
# ⁠    但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
# 
# 说明:
# 
# 
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 给定数独序列只包含数字 1-9 和字符 '.' 。
# 给定数独永远是 9x9 形式的。
# 
# 
#

# @lc code=start



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: ## 位运算
        
        rows,cols,boxes = [0]*9,[0]*9,[0]*9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    
                    boxidx = (i//3)*3 + j//3
                    row= rows[i] >> num & 1
                    col = cols[j] >> num & 1
                    box = boxes[boxidx] >> num & 1  
                    
                    if row == 1 or col == 1 or box == 1:
                        return False   
                    rows[i] = rows[i] | (1 << num)
                    cols[j] = cols[j] | (1 << num)
                    boxes[boxidx] = boxes[boxidx] | (1 << num)
        return True  
                    
                    
## 位运算: 用一个9位的二进制数来储存每次遍历到的数字，这个二进制数字的哪一位是1，就证明这个
## 数字出现过。比如 000100100,证明2、5这两个数字出现过，这样的话，每次遍历到一个新的数字m，
## 把已经储存的数字右移m位，和1做&运算，如果这个数字之前已经出现过，那么结果就是1。那就可以返回
## False.这样的话就可以用三个9位的一维数组储存，而不用三个二维数组储存。还可以直接用一个27位
## 的数组储存，这样位移的时候，分别位移 num+9,和num+9+9位即可。
                
     
                
# @lc code=end


# class Solution:
#     def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         # init data
#         rows = [{} for i in range(9)]
#         columns = [{} for i in range(9)]
#         boxes = [{} for i in range(9)]

#         # validate a board
#         for i in range(9):
#             for j in range(9):
#                 num = board[i][j]
#                 if num != '.':
#                     num = int(num)
#                     box_index = (i // 3 ) * 3 + j // 3
                    
#                     # keep the current cell value
#                     rows[i][num] = rows[i].get(num, 0) + 1
#                     columns[j][num] = columns[j].get(num, 0) + 1
#                     boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
#                     # check if this value has been already seen before
#                     if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
#                         return False         
#         return True



    # from collections import Counter
    # import numpy as np 
    # def isValidSudoku(self, board: List[List[str]]) -> bool: ## 常规hash表、或者2wei 数组
    #     rows = [[0 for j in range(9)] for i in range(9)]
    #     columns = [[0 for j in range(9)] for i in range(9)]
    #     boxes = [[0 for j in range(9)] for i in range(9)]
    #     for i in range(9):
    #         for j in range(9):
    #             num = board[i][j]
    #             if num != '.':
    #                 num = int(num) - 1 
    #                 box = (i // 3)*3 + j//3

    #                 if rows[i][num] == 0 and columns[j][num] == 0 and boxes[box][num] == 0:
    #                     rows[i][num] = 1 
    #                     columns[j][num] = 1 
    #                     boxes[box][num] = 1 
    #                 else:
    #                     return False 
 
    #     return True 
                    