#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (75.38%)
# Likes:    751
# Dislikes: 0
# Total Accepted:    312.5K
# Total Submissions: 414.4K
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
    def maxDepth(self, root: TreeNode) -> int:## 递归
        if not root:
            return 0 
        
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
# @lc code=end

    # def maxDepth(self, root: TreeNode) -> int:## 迭代
    #     if not root:
    #         return 0 
    #     cur = [(root,1)]
    #     max_depth = 0 
    #     while cur: 
    #         node,depth = cur.pop()
    #         if node.left:
    #             cur.append((node.left,depth+1))
    #         if node.right:
    #             cur.append((node.right,depth+1))
    #         max_depth = max(max_depth,depth)
    #     return max_depth 

