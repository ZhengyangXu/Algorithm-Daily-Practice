#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (62.41%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 31.6K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 您需要在二叉树的每一行中找到最大的值。
# 
# 示例：
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# 输出: [1, 3, 9]
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
    def largestValues(self, root: TreeNode) -> List[int]: ## 递归
        if not root:
            return   
        
        cur = [root]
        ans = []
        while cur:
            next_level = []
            maxvalue = float('-inf')
            for node in cur:
                if node.val >= maxvalue:
                    maxvalue = node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            ans.append(maxvalue)
            cur = next_level
        return ans   
                
                
                
    
            
        
# @lc code=end

# def largestValues(self, root: TreeNode) -> List[int]: ## 迭代 
#         if not root:
#             return   
        
#         cur = [root]
#         ans = []
#         while cur:
#             next_level = []
#             maxvalue = float('-inf')
#             for node in cur:
#                 if node.val >= maxvalue:
#                     maxvalue = node.val
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)
            
#             ans.append(maxvalue)
#             cur = next_level
#         return ans   
                