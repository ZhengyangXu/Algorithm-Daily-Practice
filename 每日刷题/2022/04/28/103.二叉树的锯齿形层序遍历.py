#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (57.29%)
# Likes:    629
# Dislikes: 0
# Total Accepted:    230K
# Total Submissions: 401.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
#
#
# 示例 2：
#
#
# 输入：root = [1]
# 输出：[[1]]
#
#
# 示例 3：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [0, 2000] 内
# -100 <= Node.val <= 100
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []

        def dfs(root, depth):
            if not root:
                return

            if len(res) == depth:
                res.append([])

            if depth % 2 == 0:
                res[depth].append(root.val)
            else:
                res[depth].insert(0, root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return res


# @lc code=end
# def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#     if not root: BFS
#         return []

#     cur = [root]
#     depth = 0
#     res = []

#     while cur:
#         size = len(cur)
#         tmp = []
#         for _ in range(size):
#             node = cur.pop(0)
#             tmp.append(node.val)
#             if node.left:
#                 cur.append(node.left)
#             if node.right:
#                 cur.append(node.right)

#         if depth % 2 == 0:
#             res.append(tmp)
#         else:
#             res.append(tmp[::-1])
#         depth += 1

#     return res
