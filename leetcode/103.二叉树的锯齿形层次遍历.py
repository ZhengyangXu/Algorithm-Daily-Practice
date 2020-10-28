#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (55.12%)
# Likes:    285
# Dislikes: 0
# Total Accepted:    76.5K
# Total Submissions: 138.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回锯齿形层次遍历如下：
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]: ## 递归
        res = []
        
        def recurse(root,depth):
            if not root:
                return   
            if len(res) == depth:
                res.append([])
                
            if depth % 2 == 0:
                res[depth].append(root.val)
            else:
                res[depth].insert(0,root.val)
                
            recurse(root.left,depth+1)
            recurse(root.right,depth+1)
            
        
        
        recurse(root,0)
        
        return res  
        
        
     
  

                
                
         
        
                         
                    
                    
                
# @lc code=end
    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]: ## 递归
    #     if not root:
    #         return []
    #     ans = []
    #     cur = [root]
    #     depth = 0 
    #     while cur:
    #         temp = [] 
    #         next = []
    #         for node in cur:
    #             temp.append(node.val)
    #             if node.left:
    #                 next.append(node.left)
    #             if node.right:
    #                 next.append(node.right)
                
    #         if depth % 2 == 0:
    #             ans.append(temp)
    #         else:
    #             ans.append(temp[::-1])
    #         depth += 1 
    #         cur = next  
    #     return ans 
    
    ## 思路：层次遍历，当深度为2的倍数时，翻转，否则暗沉呢盖茨比那里添加
