#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (61.39%)
# Likes:    425
# Dislikes: 0
# Total Accepted:    115.7K
# Total Submissions: 187.9K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 返回:
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        cur_layer = [(root,[root.val])]
        
        res = []
        while cur_layer:
            next_layer = []
            for node,path in cur_layer:
                if not node.left and not node.right and sum(path) == targetSum:
                    res.append(path)
                    
                if node.left:
                    next_layer.append((node.left,path.append(node.left.val)))
                    
                if node.right:
                    next_layer.append((node.right,path.append(node.right.val)))    
            
            
            
            cur_layer = next_layer 
            
        return res 
                    
                     
            
   
# @lc code=end


                
    # def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]: ## 回溯
    #     res = []
    #     path = []
        
    #     def dfs(root,curSum):
    #         if not root:
    #             return  
    #         path.append(root.val)
    #         curSum -= root.val 
    #         if not root.left and not root.right and curSum == 0:
    #             res.append(path[:])
                
    #         dfs(root.left,curSum)
    #         dfs(root.right,curSum)
    #         path.pop()
            
    #     dfs(root,targetSum)
    #     return res 