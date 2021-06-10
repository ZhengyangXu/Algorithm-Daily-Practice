#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (59.34%)
# Likes:    471
# Dislikes: 0
# Total Accepted:    72.6K
# Total Submissions: 116.5K
# Testcase Example:  '5\n[1,2,5]'
#
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
#
#
#
#
#
#
# 示例 1:
#
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
#
# 示例 2:
#
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
#
#
# 示例 3:
#
# 输入: amount = 10, coins = [10]
# 输出: 1
#
#
#
#
# 注意:
#
# 你可以假设：
#
#
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
#
#
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins) 
        @cache
        def dfs(cur,i):
            if cur == 0:
                return 1 
            if cur < 0 or i >= n:
                return 0 
            return dfs(cur,i+1) + dfs(cur-coins[i],i)
        return dfs(amount,0)
# @lc code=end


    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
    
    
    def change(self, amount: int, coins: List[int]) -> int: ## wrong
        n = len(coins) 
        count = 0 
        def dfs(cur):
            nonlocal count 
            if cur == 0:
                count += 1 
            if cur < 0 :
                return 0 
            for coin in coins:
                dfs(cur - coin)
        dfs(amount)
        return count 
    
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins) 
        
        dp =[[0] * (amount+1) for _ in range(n+1)]
        dp[0][0] = 1 
        for i in range(1,n+1):
            coin = coins[i-1]
            for j in range(amount+1):
                dp[i][j] = dp[i-1][j] 
                k = 1 
                while k * coin <= j:
                    dp[i][j] += dp[i-1][j-coin*k]
                    k += 1 
        return dp[n][amount] 