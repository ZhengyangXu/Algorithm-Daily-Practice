#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#
# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Medium (63.65%)
# Likes:    420
# Dislikes: 0
# Total Accepted:    65.8K
# Total Submissions: 103.2K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node
# 的新值等于原树中大于或等于 node.val 的值之和。
# 
# 提醒一下，二叉搜索树满足下列约束条件：
# 
# 
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
# 
# 
# 注意：本题和 1038:
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/
# 相同
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 
# 
# 示例 2：
# 
# 输入：root = [0,null,1]
# 输出：[1,null,1]
# 
# 
# 示例 3：
# 
# 输入：root = [1,0,2]
# 输出：[3,3,2]
# 
# 
# 示例 4：
# 
# 输入：root = [3,2,4,1]
# 输出：[7,9,4,10]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数介于 0 和 10^4^ 之间。
# 每个节点的值介于 -10^4 和 10^4 之间。
# 树中的所有值 互不相同 。
# 给定的树为二叉搜索树。
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
    def convertBST(self, root: TreeNode) -> TreeNode:## morbis
        def inorder(root):
            if not root:
                return   
            sum = 0 
            pre = None   
            while root:
                if root.right:
                    pre = root.right   
                    while pre.left  and pre.left != root:
                        pre = pre.left
                    if pre.left:
                        pre.left = None  
                        sum += root.val  
                        root.val = sum  
                        root = root.left 
                        
                        
                    
                    else:
                        pre.left = root  
                        root = root.right 
                         
                else:
                    sum += root.val  
                    root.val = sum  
                    root = root.left 
        inorder(root)
        return root 
          
                    
                    
             
            
            
        
# @lc code=end
# def convertBST(self, root: TreeNode) -> TreeNode: 中序遍历
        
#         ans = 0 
#         def inorder(root):
            
#             if not root:
#                 return
#             nonlocal ans
#             inorder(root.right)
#             ans += root.val 
#             root.val = ans
#             inorder(root.left)
        
#         inorder(root)
#         return root
#  def convertBST(self, root: TreeNode) -> TreeNode:## morbis
#         def inorder(root):
#             if not root:
#                 return   
#             sum = 0 
#             pre = None   
#             while root:
#                 if root.right:
#                     pre = root.right   
#                     while pre.left and pre.left != root:
#                         pre = pre.left   
#                     if pre.left:
#                         pre.left = None 
#                         sum += root.val 
#                         root.val = sum
#                         root = root.left 
#                     else:
#                         pre.left = root  
#                         root = root.right 
                        
                         
#                 else:
#                     sum += root.val  
#                     root.val = sum  
#                     root = root.left 
#         inorder(root)
#         return root 
          
          
## 思路：中序遍历BST是上升的序列，改变顺序，先遍历右子树，则是下降的序列。那么每个节点计算比自己大的节点的和，就是
## 这个下降序列里当前节点之前的所有节点的和。