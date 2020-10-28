#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# https://leetcode-cn.com/problems/path-sum/description/
#
# algorithms
# Easy (51.30%)
# Likes:    447
# Dislikes: 0
# Total Accepted:    144.4K
# Total Submissions: 281.6K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
# 
# 
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:## BFS
        if not root:
            return False
        
        curnode = [root]
        total = [root.val]
        
        while curnode:
            
            node =  curnode.pop() 
            cursum = total.pop() 
            if not node.left and not node.right and sum-cursum == 0:
                return True  
            if node.left:
                curnode.append(node.left)
                total.append(cursum+node.left.val) 
            if node.right:
                curnode.append(node.right)
                total.append(cursum+node.right.val)
        return False     
                
# @lc code=end
#    def hasPathSum(self, root: TreeNode, sum: int) -> bool:## 递归
#         if not root:
#             return False  
#         if not root.left and not root.right:
#             return sum == root.val
        
#         return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)


    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:## BFS
    #     if not root:
    #         return False  
        
    #     cur = [(root,sum-root.val)]
        
    #     while cur:
            
    #         node,cursum = cur.pop()
    #         if not node.left and not node.right and cursum == 0:
    #             return True   
    #         if node.left:
    #             cur.append((node.left,cursum-node.left.val))
    #         if node.right:
    #             cur.append((node.right,cursum-node.right.val))
    #     return False     
    
    ## 思路：递归或者BFS。BFS可以用两个栈，一个记录当前节点，一个记录到当前节点的路径的和。如果到了
    ##叶子结点有sum和原来的sum相等，则True，否则False.  
    
    ## 递归：判断root节点需要做的操作，然后递归。需要两个判断：是否有root，没有则false，有root的话
    ## root是否是唯一节点，是的话则判断root.val和sum，否则递归。