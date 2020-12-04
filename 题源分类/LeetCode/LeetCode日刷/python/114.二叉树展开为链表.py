#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (71.17%)
# Likes:    596
# Dislikes: 0
# Total Accepted:    88.2K
# Total Submissions: 124K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为一个单链表。
# 
# 
# 
# 例如，给定二叉树
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 将其展开为：
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    def flatten(self, root: TreeNode) -> None: ## 迭代2
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return   
        
        
        cur = root   
        
        while cur:
            if cur.left:
                pre = nxt = cur.left    
                while pre.right: 
                    pre = pre.right    
                pre.right = cur.right  
                cur.left = None  
                cur.right = nxt   
            
            cur = cur.right  
            
        return root  


            
            
            
        
        
        
# @lc code=end

    # def flatten(self, root: TreeNode) -> None: ## 递归
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     if not root:
    #         return  
        

        
        
    #     left = root.left  
    #     right = root.right 
        
    #     root.left = None 
    #     root.right = left 
        
    #     p = root  
        
    #     while p.right:
    #         p = p.right 
    #     p.right = right 
    #     self.flatten(root.left)
    #     self.flatten(root.right)
        
    #     return root 
        
        
        
#     def flatten(self, root: TreeNode) -> None: ## 迭代
#         """
#         Do not return anything, modify root in-place instead.
#         """
        
#         if not root:
#             return  
#         lis = []
#         def preorder(root):
#             if not root:
#                 return 
#             lis.append(root)
#             preorder(root.left)
#             preorder(root.right)
            
        
#         preorder(root)

#         for i in range(1,len(lis)):
#             prev,cur = lis[i-1],lis[i]
            
#             prev.left = None  
#             prev.right = cur 
            
#         return root  


# ### 思路:整棵树前序遍历添加到list中就是之后的树的顺序，然后形成右斜树 。这种做法分了两步，原有的树的结构会被打乱。  




# def flatten(self, root: TreeNode) -> None: ## 迭代2
#         """
#         Do not return anything, modify root in-place instead.
#         """
        
#         if not root:
#             return   
        
#         stack = [root]
#         pre = None  
        
#         while stack:
            
#             cur = stack.pop()
            
#             if pre:
#                 pre.left = None  
#                 pre.right = cur   
#             if cur.right:
#                 stack.append(cur.right)
#             if cur.left:
#                 stack.append(cur.left) 
            
#             pre = cur   
        
#         return root 
             
             

### 思路:不用把整个树打乱在重新构成，而是一边剔除左子树，一边重新构成树。用一个pre节点保存之前的节点，之前节点的左
### 子树为null，右子树为curr