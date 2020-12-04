#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (70.68%)
# Likes:    388
# Dislikes: 0
# Total Accepted:    74.4K
# Total Submissions: 105.2K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def construct(inorder,inl,inr,postorder,pol,por):
            if inl > inr or pol > por:
                return 
            
            root = TreeNode(postorder[por])
            
            index = 0
            
            for i in range(inl,inr+1):
                if root.val == inorder[i]:
                    index = i  
                    break
                
            leftsize = index - inl   
            
            root.left = construct(inorder,inl,index-1,postorder,pol,pol+leftsize-1)
            root.right = construct(inorder,index+1,inr,postorder,pol+leftsize,por-1)
            
            return root   
        
        return construct(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1) 
# @lc code=end

