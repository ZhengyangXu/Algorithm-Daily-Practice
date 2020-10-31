#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (65.62%)
# Likes:    548
# Dislikes: 0
# Total Accepted:    47.2K
# Total Submissions: 71.8K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int: ## 递归带memo，也超时？？？？
        if n == 1 or n == 0:
            return 1  
        memo = [0]*(n+1)
        
        if memo[n] != 0:
            return memo[n]
        
        for i in range(1,n+1):
            memo[n] += self.numTrees(i-1)*self.numTrees(n-i)
        
        return memo[n]
        
        
        
 
        
          
# @lc code=end

# class Solution:
#     def numTrees(self, n: int) -> int: # DP
#         G = [0] * (n+1)
#         G[0],G[1] = 1,1 
        
#         for i in range(2,n+1):
#             for j in range(1,i+1):
#                 G[i] += G[j-1] * G[i-j]
                
#         return G[n]


#  def numTrees(self, n: int) -> int: ## 递归超时
#         if n == 1 or n==0:
#             return 1
#         ans = 0 
#         for i in range(1,n+1):
#             ans += self.numTrees(i-1) * self.numTrees(n-i)
#         return ans 