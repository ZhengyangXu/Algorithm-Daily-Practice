#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (68.32%)
# Likes:    723
# Dislikes: 0
# Total Accepted:    123.4K
# Total Submissions: 180.5K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
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

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode: ## 递归
        
    #     def construct(preorder,prel,preh,inorder,inl,inh):
            
    #         if prel > preh or inl > inh:
    #             return    
    #         root = TreeNode(preorder[prel])
            
    #         index = -1 
    #         for i in range(inl,inh+1):
    #             if inorder[i] == root.val:
    #                 index = i  
    #                 break   
                
    #         leftsize = index - inl    
    #         root.left = construct(preorder,prel+1,prel+leftsize,inorder,inl,index-1)
    #         root.right = construct(preorder,prel+1+leftsize,preh,inorder,index+1,inh)
            
    #         return root    
    #     return construct(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode: ## 迭代
        if not preorder:
            return None 
        
        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in  range(1,len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1 
                node.right = TreeNode(preorderVal)
                stack.append(node.right)
        return root 
        
        

        
                    
# @lc code=end

