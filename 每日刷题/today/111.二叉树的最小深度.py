#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode.cn/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (50.27%)
# Likes:    746
# Dislikes: 0
# Total Accepted:    387.4K
# Total Submissions: 770.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明：叶子节点是指没有子节点的节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#
#
#
#
# 提示：
#
#
# 树中节点数的范围在 [0, 10^5] 内
# -1000
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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        cur = [(root, 1)]

        while cur:
            node, depth = cur.pop(0)
            #
            if node.left:
                cur.append((node.left, depth + 1))
            if node.right:
                cur.append((node.right, depth + 1))

            if not node.left and not node.right:
                return depth


# @lc code=end
# def minDepth(self, root: TreeNode) -> int:
#     if not root:
#         return 0
#     if not root.left:
#         return self.minDepth(root.right) + 1
#     if not root.right:
#         return self.minDepth(root.left) + 1

#     return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
