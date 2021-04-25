#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (71.81%)
# Likes:    544
# Dislikes: 0
# Total Accepted:    180.4K
# Total Submissions: 251.1K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [1,3,2]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return root

        pre = None
        res = []
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root
                tmp = root
                root = root.left
                tmp.left = None
            else:
                res.append(root.val)
                root = root.right
        return res


# @lc code=end
# def inorderTraversal(self, root: TreeNode) -> List[int]:
#     res = []
#     stack = []
#     node = root
#     while stack or node:
#         if node:
#             stack.append(node)
#             node = node.left
#         else:
#             tmp = stack.pop()
#             res.append(tmp.val)
#             node = tmp.right
#     return res  recursion

## 莫比斯遍历？？？
# def inorderTraversal(self, root: TreeNode) -> List[int]:
# res = []
# pre = None
# while root:
#     if root.left:
#         pre = root.left
#         while pre.right:
#             pre = pre.right
#         pre.right = root
#         tmp = root
#         root = root.left
#         tmp.left = None
#     else:
#         res.append(root.val)
#         root = root.right
# return res
## recursion
# def inorderTraversal(self, root: TreeNode) -> List[int]:
#     res = []
#     def helper(root):
#         if not root:
#             return
#         helper(root.left)
#         res.append(root.val)
#         helper(root.right)
#     helper(root)
#     return res
