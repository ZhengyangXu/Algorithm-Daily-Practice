#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (42.69%)
# Likes:    289
# Dislikes: 0
# Total Accepted:    89K
# Total Submissions: 207.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0  
        
      
        cur = [(root,1)]
        
        while cur: 
            node,depth = cur.pop(0)
            if node.left:
                cur.append((node.left,depth+1))
            if node.right:
                cur.append((node.right,depth+1))
            if not node.left and not node.right:
                return depth  
            

                
        
# @lc code=end

    # def minDepth(self, root: TreeNode) -> int: 迭代
    #     if not root:
    #         return 0
        
    #     queue = [[root]] 
    #     depth = 1
    #     while queue:
    #         nodes = queue.pop(0)
    #         children = []
    #         for cur in nodes:
    #             if not cur.left and not cur.right:
    #                 return depth 
    #             if cur.left:
    #                 children.append(cur.left)
    #             if cur.right:
    #                 children.append(cur.right)
    #         depth += 1
    #         queue.append(children)
    #     return depth

    # def minDepth(self, root: TreeNode) -> int:#递归
    #     if not root:
    #         return 0 
    #     if not root.left:
    #         return self.minDepth(root.right) + 1 
    #     if not root.right:
    #         return self.minDepth(root.left) + 1 
    #     return min(self.minDepth(root.right),self.minDepth(root.left)) + 1