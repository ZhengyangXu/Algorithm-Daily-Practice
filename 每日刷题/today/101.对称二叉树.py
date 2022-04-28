#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (57.51%)
# Likes:    1885
# Dislikes: 0
# Total Accepted:    574.3K
# Total Submissions: 997.9K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
#
#
#
#
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ##迭代，层序遍历

        if not root:
            return True

        cur = [root]

        while any(cur):
            next_layer = []
            i, j = 0, len(cur) - 1
            while i < j:
                if not (cur[i] or cur[j]):
                    i += 1
                    j -= 1
                    continue
                if (not cur[i]) ^ (not cur[j]):
                    return False
                if cur[i] and cur[j] and cur[i].val != cur[j].val:
                    return False
                i += 1
                j -= 1

            for node in cur:
                if node:
                    next_layer.append(node.left)
                    next_layer.append(node.right)

            cur = next_layer
        return True


# @lc code=end

# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#     ##递归
#     if not root:
#         return True

#     def isSymmetric(left,right):
#         if not left and not right:
#             return True

#         if (not left) ^ (not right):
#             return False

#         if left.val != right.val:
#             return False

#         return isSymmetric(left.left,right.right) and isSymmetric(left.right,right.left)

#     return isSymmetric(root.left,root.right)

# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#     ##迭代，层序遍历

#     if not root:
#         return True

#     cur = [root]

#     while any(cur):
#         next_layer = []
#         i, j = 0, len(cur) - 1
#         while i < j:
#             if (not cur[i]) ^ (not cur[j]):
#                 return False
#             if cur[i] and cur[j] and cur[i].val != cur[j].val:
#                 return False
#             i += 1
#             j -= 1

#         for node in cur:
#             next_layer.append(node.left if node else None)
#             next_layer.append(node.right if node else None)

#         cur = next_layer
#     return True

# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#     ##迭代，层序遍历

#     if not root:
#         return True

#     q = [root.left, root.right]

#     while q:
#         left, right = q.pop(0), q.pop(0)

#         if (not left) ^ (not right):
#             return False
#         if not (left or right):
#             continue
#         if left.val != right.val:
#             return False
#         q.append(left.left)
#         q.append(right.right)
#         q.append(left.right)
#         q.append(right.left)

#     return True
