#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#
# https://leetcode-cn.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (44.23%)
# Likes:    321
# Dislikes: 0
# Total Accepted:    24.4K
# Total Submissions: 54.9K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key
# 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
# 
# 一般来说，删除节点可分为两个步骤：
# 
# 
# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 
# 
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
# 
# 示例:
# 
# 
# root = [5,3,6,2,4,null,7]
# key = 3
# 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
# 
# ⁠   5
# ⁠  / \
# ⁠ 4   6
# ⁠/     \
# 2       7
# 
# 另一个正确答案是 [5,2,6,null,4,null,7]。
# 
# ⁠   5
# ⁠  / \
# ⁠ 2   6
# ⁠  \   \
# ⁠   4   7
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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode: ## 递归，用左子树最大值替换删除值
        def getmax(node):
            while node.right:
                node = node.right  
            return node   
        
        if not root:
            return  
        if root.val == key:
            if not (root.left and root.right):
                return root.left if root.left else root.right  
            else:
                maxnode = getmax(root.left)
                root.val = maxnode.val  
                
                root.left = self.deleteNode(root.left,maxnode.val)
                
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
            
        else:
            root.right = self.deleteNode(root.right,key)
        
        return root                  
        
# @lc code=end

    # def deleteNode(self, root: TreeNode, key: int) -> TreeNode: ## 递归，用右子树最小值替换删除值
    #     def getmin(node):
    #         while node.left:
    #             node = node.left  
    #         return node   
        
    #     if not root:
    #         return   
    #     if root.val == key:
    #         if not (root.left and root.right):
    #             return root.left if root.left else root.right  
    #         else:
    #             minnode = getmin(root.right)
    #             root.val = minnode.val  
                
    #             root.right = self.deleteNode(root.right,minnode.val)
    #     elif root.val > key:
    #         root.left = self.deleteNode(root.left,key)
    #     else:
    #         root.right = self.deleteNode(root.right,key)
            
    #     return root   