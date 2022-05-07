#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (72.37%)
# Likes:    736
# Dislikes: 0
# Total Accepted:    191K
# Total Submissions: 263.9K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder
# 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
#
#
#
# 示例 1:
#
#
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
#
#
# 示例 2:
#
#
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#
#
#
#
# 提示:
#
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder 和 postorder 都由 不同 的值组成
# postorder 中每一个值都在 inorder 中
# inorder 保证是树的中序遍历
# postorder 保证是树的后序遍历
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        #迭代
        if not postorder or len(postorder) == 0:
            return
        root = TreeNode(postorder[-1])
        stack = []
        stack.append(root)

        start = len(inorder) - 1
        for i in range(len(postorder) - 2, -1, -1):
            postval = postorder[i]
            node = stack[-1]
            if node.val != inorder[start]:
                node.right = TreeNode(postval)
                stack.append(node.right)
            else:
                while stack and stack[-1].val == inorder[start]:
                    node = stack.pop()
                    start -= 1
                node.left = TreeNode(postval)
                stack.append(node.left)
        return root


# @lc code=end
# def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode: //递归
#     if not inorder or not postorder:
#         return

#     root = TreeNode(postorder[-1])

#     for i in range(len(inorder)):
#         if inorder[i] == root.val:
#             index = i
#             break

#     root.left = self.buildTree(inorder[:index], postorder[:index])
#     root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])

#     return root
