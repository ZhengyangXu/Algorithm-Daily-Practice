#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (71.76%)
# Likes:    1188
# Dislikes: 0
# Total Accepted:    128.1K
# Total Submissions: 178.4K
# Testcase Example:  '3'
#
# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
#
#
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：[[1]]
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
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def buildTree(l, r):
            if l > r:
                return [
                    None,
                ]
            allTrees = []
            for i in range(l, r + 1):
                left = buildTree(l, i - 1)
                right = buildTree(i + 1, r)

                for lt in left:
                    for rt in right:
                        curNode = TreeNode(i)
                        curNode.left = lt
                        curNode.right = rt
                        allTrees.append(curNode)
            return allTrees

        return buildTree(1, n) if n else []


# @lc code=end
