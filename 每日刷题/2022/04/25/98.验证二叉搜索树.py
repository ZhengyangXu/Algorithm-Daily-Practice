#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (35.91%)
# Likes:    1541
# Dislikes: 0
# Total Accepted:    490K
# Total Submissions: 1.4M
# Testcase Example:  '[2,1,3]'
#
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
#
#
# 示例 1：
#
#
# 输入：root = [2,1,3]B
# 输出：true
#
#
# 示例 2：
#
#
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#
#
#
#
# 提示：
#
#
# 树中节点数目范围在[1, 10^4] 内
# -2^31 <= Node.val <= 2^31 - 1
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, lower=-float('inf'), upper=float('inf')):
            if not root:
                return True

            if root.val <= lower or root.val >= upper:
                print("root为%i" % root.val)
                return False

            if not isValid(root.left, lower, root.val):
                print("root为%i左子树有问题" % root.val)
                return False

            if not isValid(root.right, root.val, upper):
                print("root为%i右子树有问题" % root.val)
                return False

            return True

        return isValid(root)


# @lc code=end
# def isValidBST(self, root: Optional[TreeNode]) -> bool:
#     def isValidBST(root, left, right):
#         if not root:
#             return True

#         if left and root.val <= left.val:
#             return False

#         if right and root.val >= right.val:
#             return False

#         return isValidBST(root.left, left, root) and isValidBST(
#             root.right, root, right)

#     return isValidBST(root, None, None)

# def isValidBST(self, root: Optional[TreeNode]) -> bool:
#     #res = []
#     pre = -float('inf')
#     stack = []

#     while root or stack:
#         while root:
#             stack.append(root)
#             root = root.left
#         root = stack.pop()
#         if root.val <= pre:
#             return False
#         pre = root.val
#         root = root.right
#     return True
