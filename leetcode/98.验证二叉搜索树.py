#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (31.52%)
# Likes:    641
# Dislikes: 0
# Total Accepted:    135.7K
# Total Submissions: 429.6K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
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
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(root,small,big):
            
            if not root:
                return True 
            
            if root.val > small and root.val < big:
                return helper(root.left,small,root.val) and helper(root.right,root.val,big)
            else:
                return False 
            
            return True  
        
        return helper(root,float('-inf'),float('inf'))

            

            
# @lc code=end

    # def isValidBST(self, root: TreeNode) -> bool:
    #     val = float('-inf')
    #     stack = []
    #     node = root
    #     while stack or node:
    #         if node:
    #             stack.append(node)
    #             node = node.left 
    #         else:
    #             tmp = stack.pop()
    #             if tmp.val <= val:
    #                 return False
    #             val = tmp.val  
    #             node = tmp.right
    #     return True 
    # 中序遍历
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def helper(root,upper,lower):
    #         if not root:
    #             return True 
    #         if root.val > lower and root.val < upper:
    #             return helper(root.left,root.val,lower) and helper(root.right,upper,root.val)
    #         else:
    #             return False 
    #     return helper(root,float('inf'),float('-inf'))