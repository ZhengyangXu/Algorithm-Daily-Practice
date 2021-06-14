#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (40.08%)
# Likes:    693
# Dislikes: 0
# Total Accepted:    100.8K
# Total Submissions: 250.6K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
#
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
#
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
#
#
# 说明:
# 你可以认为每种硬币的数量是无限的。
#
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ##
        if not coins or not amount:
            return 0
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i],dp[i-coin]+1)

        return dp[amount] if dp[amount] != float('inf') else -1




# @lc code=end
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## 递归
        memo = dict()
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('inf')
            for coin in coins:
                sub = dp(n - coin)
                if sub == -1: continue
                res = min(res, sub + 1)
            memo[n] = res if res != float('inf') else -1
            return memo[n]
        return dp(amount)



    def coinChange(self, coins: List[int], amount: int) -> int:
        ##
        from functools import lru_cache
        @lru_cache(amount)
        def dp(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            res = float('inf')

            for coin in coins:
                sub = dp(amount - coin)
                if sub == -1: continue
                res = min(res, sub + 1)
            return res if res != float('inf') else -1
        return dp(amount)
    
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        ##
        if not coins or not amount:
            return 0
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)

        return dp[amount] if dp[amount] != float('inf') else -1