#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (75.77%)
# Likes:    1399
# Dislikes: 0
# Total Accepted:    790.9K
# Total Submissions: 1M
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#
#
# 示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
#
#
#
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from numpy import roots


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #迭代
        res = []

        if not root:
            return []

        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


# @lc code=end
# def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     #递归：
#     res = []

#     def dfs(root):
#         if not root:
#             return
#         dfs(root.left)
#         res.append(root.val)
#         dfs(root.right)

#     dfs(root)

#     return res
