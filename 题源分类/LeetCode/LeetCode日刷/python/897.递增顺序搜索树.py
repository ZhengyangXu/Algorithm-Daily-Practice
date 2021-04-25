#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#
# https://leetcode-cn.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (72.57%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    44.1K
# Total Submissions: 59.1K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# 给你一棵二叉搜索树，请你 按中序遍历
# 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#
# 示例 2：
#
#
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
#
#
#
#
# 提示：
#
#
# 树中节点数的取值范围是 [1, 100]
# 0
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
    def increasingBST(self, root: TreeNode) -> TreeNode: ## morbis环
        if not root:
            return root
        
        pre = None 
        first = TreeNode(-1)
        last = first 
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
                last.right = root #
                last = root 
                root = root.right 
        return first.right 
        




# @lc code=end

# def increasingBST(self, root: TreeNode) -> TreeNode:
#     prev = TreeNode(-1)
#     dummy = prev

#     def inorder(root):
#         nonlocal prev
#         if not root:
#             return None
#         inorder(root.left)
#         root.left = None
#         prev.right = root
#         prev = root
#         inorder(root.right)

#     inorder(root)

#     return dummy.right

# def increasingBST(self, root: TreeNode) -> TreeNode:
#     if not root:
#         return root

#     node = root
#     stack = []
#     prev = TreeNode(-1)
#     dummy = prev
#     while node or stack:
#         if node:
#              stack.append(node)
#              node = node.left
#         else:
#             node = stack.pop()
#             node.left = None
#             prev.right = node
#             prev = node
#             node = node.right

#     return dummy.right
