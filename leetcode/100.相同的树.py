#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (58.05%)
# Likes:    386
# Dislikes: 0
# Total Accepted:    97.4K
# Total Submissions: 167.7K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 示例 1:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# 输出: true
# 
# 示例 2:
# 
# 输入:      1          1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# 输出: false
# 
# 
# 示例 3:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# 输出: false
# 
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True 
        if not (p and q):
            return False  
        if p.val != q.val:
            return False  
        stackp = [p]
        stackq = [q]
        while stackp and stackq:
            nodep = stackp.pop()
            nodeq = stackq.pop()
            if not (nodep or nodeq):
                continue 
            if not (nodep and nodeq):
                return False 
            
            if nodep.val != nodeq.val:
                return False 
            
            stackp.append(nodep.left)
            stackq.append(nodeq.left)
            stackp.append(nodep.right)
            stackq.append(nodeq.right)
        return True
            
# @lc code=end
# class Solution: recursion
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if not p and not q:
#             return True  
#         if not (p and q):
#             return False
#         if p.val != q.val:
#             return False 
#         return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
