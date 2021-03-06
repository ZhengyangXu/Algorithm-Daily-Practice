#
# @lc app=leetcode.cn id=1269 lang=python3
#
# [1269] 停在原地的方案数
#
# https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/description/
#
# algorithms
# Hard (40.85%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    18.5K
# Total Submissions: 38.2K
# Testcase Example:  '3\n2'
#
# 有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。
# 
# 每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。
# 
# 给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。
# 
# 由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。
# 
# 
# 
# 示例 1：
# 
# 输入：steps = 3, arrLen = 2
# 输出：4
# 解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
# 向右，向左，不动
# 不动，向右，向左
# 向右，不动，向左
# 不动，不动，不动
# 
# 
# 示例  2：
# 
# 输入：steps = 2, arrLen = 4
# 输出：2
# 解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
# 向右，向左
# 不动，不动
# 
# 
# 示例 3：
# 
# 输入：steps = 4, arrLen = 2
# 输出：8
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= steps <= 500
# 1 <= arrLen <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7 
        
        maxcol = min(steps//2,arrLen-1)
        dp = [0 for _ in range(maxcol+1)]
        dp[0] = 1 
        
        for i in range(1,steps+1):
            edge = min(maxcol,i)
            dpnex = [0 for _ in range(maxcol+1)]
            for j in range(edge+1):
                dpnex[j] = dp[j]
                if j - 1 >= 0:
                    dpnex[j] = (dp[j-1]+dpnex[j]) % mod 
                if j + 1 <= edge:
                    dpnex[j] = (dp[j+1]+dpnex[j]) % mod
                    
            dp = dpnex 
        return dp[0] 
        
        

         
        
# @lc code=end

    # def numWays(self, steps: int, arrLen: int) -> int:
    #     mod = 10**9 + 7 
    #     maxcol = min(steps,arrLen-1)
        
    #     dp = [[0 for _ in range(maxcol+1)] for _ in range(steps+1)]
        
    #     dp[0][0] = 1 
        
    #     for i in range(1,steps+1):
    #         for j in range(maxcol+1):
    #             dp[i][j] = dp[i-1][j]
    #             if j - 1 >= 0:
    #                 dp[i][j] = (dp[i][j]+dp[i-1][j-1])%mod 
    #             if j + 1 <= maxcol:
    #                 dp[i][j] = (dp[i][j] + dp[i-1][j+1])%mod 
        
    #     return dp[steps][0]
    
    
    
    # class Solution:  ##空间复杂度优化
    # def numWays(self, steps: int, arrLen: int) -> int:
    #     mod = 10**9 + 7 
    #     maxcol = min(steps,arrLen-1)
        
    #     dp1 = [0 for _ in range(maxcol+1)]
    #     dp1[0] = 1 
        
        
    #     for i in range(1,steps+1):
    #         dp2 = [0 for _ in range(maxcol+1)]
    #         for j in range(maxcol+1):
    #             dp2[j] = dp1[j]
    #             if j - 1 >= 0:
    #                 dp2[j] = (dp2[j]+dp1[j-1])%mod 
    #             if j + 1 <= maxcol:
    #                 dp2[j] = (dp2[j] + dp1[j+1])%mod 
    #         dp1 = dp2 
                
        
    #     return dp1[0]
    
    
        # def numWays(self, steps: int, arrLen: int) -> int: ##时间复杂度优化
        # mod = 10**9 + 7 
        # maxcol = min(steps//2,arrLen-1)
        # dp = [[0 for _ in range(maxcol+1)] for _ in range(steps+1)]
        # dp[0][0] = 1  
        # for i in range(1,steps+1):
        #     edge = min(i,maxcol)
        #     for j in range(edge+1):
        #         dp[i][j] = dp[i-1][j]
        #         if j - 1 >= 0:
        #             dp[i][j] = (dp[i-1][j-1] + dp[i][j]) % mod 
        #         if j + 1 <= maxcol:
        #             dp[i][j] = (dp[i-1][j+1] + dp[i][j]) % mod 
                
        # return dp[steps][0]