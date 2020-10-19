#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (49.84%)
# Likes:    703
# Dislikes: 0
# Total Accepted:    140.3K
# Total Submissions: 280.6K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1:
# 
# 输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
# 
# 
#

# @lc code=start
class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        count = 0 
        points = []
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    count += 1 
                    grid[x][y] = "0"
                    points.append((x,y))
                
                while points:
                    x,y = points.pop()
                    for xx,yy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                        if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == "1":
                            grid[xx][yy] = "0"
                            points.append((xx,yy))
        return count 

            
    
                    
                    
                
            

     
                    
                    
                
                
        
# @lc code=end
    #def numIslands(self, grid: List[List[str]]) -> int: DFS
        # directions = [(-1,0),(1,0),(0,-1),(0,1)]
        # rows = len(grid)
        # if rows == 0:
        #     return 0
        # cols = len(grid[0])
        
        # def dfs(grid,x,y):
        #     if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
        #         grid[x][y] = "0"
        #         for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
        #             dfs(grid,x+i,y+j)
                    
        # count = 0 
        # for x in range(rows):
        #     for y in range(cols):
        #         if grid[x][y] == "1":
        #             count += 1 
        #             dfs(grid,x,y)
                    
        # return count 
