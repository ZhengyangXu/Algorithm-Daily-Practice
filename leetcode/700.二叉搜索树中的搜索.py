#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#
# https://leetcode-cn.com/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (74.70%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    39.2K
# Total Submissions: 52.5K
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
# 
# 例如，
# 
# 
# 给定二叉搜索树:
# 
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# 
# 和值: 2
# 
# 
# 你应该返回如下子树:
# 
# 
# ⁠     2     
# ⁠    / \   
# ⁠   1   3
# 
# 
# 在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
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
    def searchBST(self, root: TreeNode, val: int) -> TreeNode: ## 递归
        
        if not root:
            return 
        
        if root.val == val:
            return root  
        
        elif root.val > val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
        
# @lc code=end

    # def searchBST(self, root: TreeNode, val: int) -> TreeNode: ## 迭代
        
    #     if not root:
    #         return 
        
    #     cur = root 
        
    #     while cur:  
    #         if cur.val == val:
    #             return cur   
    #         elif cur.val > val:
    #             cur = cur.left    
    #         else:
    #             cur = cur.right
        
    #     return None