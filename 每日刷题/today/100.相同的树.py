#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (59.73%)
# Likes:    820
# Dislikes: 0
# Total Accepted:    330.9K
# Total Submissions: 554K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
#
#
# 示例 1：
#
#
# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：p = [1,2], q = [1,null,2]
# 输出：false
#
#
# 示例 3：
#
#
# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# 两棵树上的节点数目都在范围 [0, 100] 内
# -10^4
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        #bfs
        if not p and not q:
            return True
        if not p or not q:
            return False

        pqueue = [p]
        qqueue = [q]

        while pqueue and qqueue:
            pnode = pqueue.pop(0)
            qnode = qqueue.pop(0)
            if pnode.val != qnode.val:
                return False
            pleft, pright = pnode.left, pnode.right
            qleft, qright = qnode.left, qnode.right

            if (not pleft) ^ (not qleft):
                return False
            if (not pright) ^ (not qright):
                return False

            if pleft:
                pqueue.append(pleft)

            if qleft:
                qqueue.append(qleft)

            if pright:
                pqueue.append(pright)

            if qright:
                qqueue.append(qright)

        return not pqueue and not qqueue


# @lc code=end
# def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#     def inorder(root, res):  //错误解法

#         if not root:
#             return

#         inorder(root.left, res)
#         res.append(root)
#         inorder(root.right, res)

#         return res

#     return inorder(p, []) == inorder(q, [])

# def isSameTree(self, p: TreeNode, q: TreeNode) -> bool: //深度搜索

#     if not p and not q:
#         return True

#     if not p or not q:
#         return False

#     if p.val != q.val:
#         return False

#     return self.isSameTree(p.left, q.left) and self.isSameTree(
#         p.right, q.right)
