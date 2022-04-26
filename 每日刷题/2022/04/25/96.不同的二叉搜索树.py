#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (70.15%)
# Likes:    1720
# Dislikes: 0
# Total Accepted:    236.8K
# Total Submissions: 337.6K
# Testcase Example:  '3'
#
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：5
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：1
#
#
#
#
# 提示：
#
#
# 1
#
#
#


# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        


# @lc code=end
# def numTrees(self, n: int) -> int: 递归超时
#     def buildTree(start, end):
#         cnt = 0
#         if start > end:
#             return 1
#         for i in range(start, end + 1):
#             left = buildTree(start, i - 1)
#             right = buildTree(i + 1, end)

#             cnt += left * right

#         return cnt

#     return  buildTree(1, n) if n else 0


# class Solution:
#     def numTrees(self, n: int) -> int: ##代memo的递归
#         memo = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

#         def buildTree(start, end):
#             cnt = 0
#             if start > end:
#                 return 1
#             if memo[start][end] != 0:
#                 return memo[start][end]
#             for i in range(start, end + 1):
#                 left = buildTree(start, i - 1)
#                 right = buildTree(i + 1, end)

#                 cnt += left * right

#             memo[start][end] = cnt

#             return cnt

#         return buildTree(1, n)