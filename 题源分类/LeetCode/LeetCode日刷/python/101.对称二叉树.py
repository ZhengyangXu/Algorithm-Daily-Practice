#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (52.29%)
# Likes:    879
# Dislikes: 0
# Total Accepted:    167K
# Total Submissions: 319.2K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# 进阶：
# 
# 你可以运用递归和迭代两种方法解决这个问题吗？
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
    def isSymmetric(self, root: TreeNode) -> bool:
        
        # if not root:
        #     return True 
        
 
        # def isSy(left,right):
            
        #     if not (left and right):
        #         return False 
        #     if left.val != right.val:
        #         return False 
            
        #     if not (left or right):
        #         return True 
            
        #     return isSy(left.left,right.right) and isSy(left.right,right.left)
        
        # return isSy(root.left,root.right)
        
        if not root:
            return True
        
        def dfs(left,right):
            
            if not(left or right):
                return True 
            
            if not(left and right):
                return False 

            if left.val != right.val:
                return False
            
            return dfs(left.left,right.right) and dfs(left.right,right.left)
        
        return dfs(root.left,root.right)

                
                
                
                
                
                
             
            
                
            
            
# @lc code=end

# if not root or not(root.left or root.right):
        #     return True 
        # if not (root.left and root.right):
        #     return False
        # left = [root.left]
        # right = [root.right]
        # while left and right:
        #     leftnode = left.pop()
        #     rightnode = right.pop()
        #     if leftnode.val != rightnode.val:
        #         return False 
        #     if leftnode.left and not rightnode.right:
        #         return False
        #     if leftnode.right and not rightnode.left:
        #         return False
        #     if not leftnode.left and rightnode.right:
        #         return False
        #     if not leftnode.right and rightnode.left:
        #         return False
            
        #     if leftnode.left and rightnode.right:
        #         left.append(leftnode.left)
        #         right.append(rightnode.right)
        #     else:
        #         return False
        #     if leftnode.right and rightnode.left:
        #         left.append(leftnode.right)
        #         right.append(rightnode.left)
        #     else:
        #         return False
        # return not left and not right
        
        
        # def isSymmetric(self, root: TreeNode) -> bool:
        # if not root or not(root.left or root.right): 
        #     return True 
        # queue = [root.left,root.right]
        # while queue:
        #     left = queue.pop(0)
        #     right = queue.pop(0)
        #     if not (left or right):
        #         continue
        #     if not (left and right):
        #         return False
        #     if left.val != right.val:
        #         return False  
              
        #     queue.append(left.left)
        #     queue.append(right.right)
        #     queue.append(left.right)
        #     queue.append(right.left)
        # return True