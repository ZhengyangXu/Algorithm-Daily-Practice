#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (76.93%)
# Likes:    1221
# Dislikes: 0
# Total Accepted:    708.9K
# Total Submissions: 921.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最大深度 3 。
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth


# @lc code=end
# def dfs(root, depth):
#     if not root:
#         return depth
#     depth += 1

#     return max(dfs(root.left, depth), dfs(root.right, depth))

# return dfs(root, 0) 深度搜索

# def maxDepth(self, root: Optional[TreeNode]) -> int:

#     if not root:
#         return 0

#     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# def maxDepth(self, root: Optional[TreeNode]) -> int:

#     if not root:
#         return 0

#     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 ## 动态规划，自底向上
