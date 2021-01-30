# [剑指 Offer 第 2 版第 47 题] “礼物的最大值”做题记录
# 第 47 题：礼物的最大价值
# 传送门：礼物的最大价值，牛客网 online judge 地址。

# 在一个 m×n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。

# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格直到到达棋盘的右下角。

# 给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？

# 注意：

# m,n>0
# 样例：

# 输入： [ [2,3,1], [1,7,1], [4,6,1] ]

# 输出：19

# 解释：沿着路径 2→3→7→6→1 可以得到拿到最大价值礼物。

def getMaxValue(grid):
    row = len(grid)
    col = len(grid[0])
    if not row:
        return 0  
    dp = [None for _ in range(col)]
    
    dp[0] = grid[0][0]
    for i in range(1,col):
        dp[i] = dp[i-1] + grid[0][i]
    
    for i in range(1,row):
        for j in range(col):
            if j == 0:
                dp[j] += grid[i][0]
            else:
                dp[j] = grid[i][j] + max(dp[j-1],dp[j])
    return dp[col-1]


def getMaxPresent(grid):
    if not grid:
        return 0 
    row = len(grid)
    col = len(grid[0])
    dp = [[[0] for _ in range(col)] for _ in range(row)]
    
    dp[0][0] = grid[0][0]
    
    for i in range(1,row):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    for i in range(1,col):
        dp[0][i] = dp[0][i-1] + grid[0][i]
        
    for i in range(1,row):
        for j in range(1,col):
            dp[i][j] = grid[i][j] + max(dp[i-1][j],dp[i][j-1])
            
    return dp[row-1][col-1]
            


if __name__ == "__main__":
    grid = [[2,3,1],[1,7,1],[4,6,1],[4,1,9]]
    
    print(getMaxValue(grid))
    print(getMaxPresent(grid))
        
            
    