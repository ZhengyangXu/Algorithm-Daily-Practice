#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (67.75%)
# Likes:    371
# Dislikes: 0
# Total Accepted:    111.8K
# Total Submissions: 164.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其自底向上的层次遍历为：
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        res = []
        def dfs(root,depth):
            if not root:
                return 
            
            if len(res) < depth:
                res.append([])
                
            res[depth-1].append(root.val)
            
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        
        dfs(root,1)
        return res[::-1]  
            
                    
                    
                
# @lc code=end

    # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]: ##
    #     if not root:
    #         return []
    #     cur = [root]
    #     res = []

    #     while cur: 
    #         temp = []
    #         next = []
    #         for node in cur:
    #             if node.left:
    #                 next.append(node.left)
    #             if node.right:
    #                 next.append(node.right)
    #             temp.append(node.val)
    #         res.insert(0,temp)
    #         cur = next  
    #     return res 
                    