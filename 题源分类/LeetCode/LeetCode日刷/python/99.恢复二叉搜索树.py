#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# https://leetcode-cn.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (62.04%)
# Likes:    418
# Dislikes: 0
# Total Accepted:    48.1K
# Total Submissions: 77.4K
# Testcase Example:  '[1,3,null,null,2]'
#
# 给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
# 
# 进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,3,null,null,2]
# 输出：[3,1,null,null,2]
# 解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [3,1,4,null,null,2]
# 输出：[2,1,4,null,null,3]
# 解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
# 
# 
# 
# 提示：
# 
# 
# 树上节点的数目在范围 [2, 1000] 内
# -2^31 
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
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        x,y,pre,tmp = None,None,None,None 
        
        while root:
            if root.left:
                tmp = root.left 
                while tmp.right and tmp.right != root:
                    tmp = tmp.right 
                
                if not tmp.right:
                    tmp.right = root  
                    root = root.left 
                    
                else:
                    if pre and pre.val > root.val:
                        y = root  
                        if not x:
                            x = pre 
                    pre = root 
                    tmp.right = None 
                    root = root.right 
            else:
                if pre and pre.val > root.val:
                    y = root 
                    if not x:
                        x = pre 
                pre = root 
                root = root.right 
        if x and y:
            x.val,y.val = y.val,x.val 

        
     
# @lc code=end

#   def recoverTree(self, root: TreeNode) -> None:  常规中序遍历
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         stack = []
#         node = root 
#         pre = TreeNode(float('-inf'))
#         count = 0 
#         while node or stack:
#             if node:
#                 stack.append(node)
#                 node = node.left
#             else:
#                 node = stack.pop()
#                 if count == 0 and pre.val > node.val:
#                     first = pre
#                     count += 1 
#                 if count == 1 and pre.val > node.val:
#                     second = node 
                
#                 pre = node 
                    
#                 node = node.right
#         first.val,second.val = second.val,first.val 
#         return root  


#    def recoverTree(self, root: TreeNode) -> None:  递归
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         stack = []
#         node = root 
#         first = None 
#         second = None
#         pre = TreeNode(float('-inf'))
        
#         def inorder(root,count,pre): 
#             if not root or count == 1:
#                 return 
#             inorder(root.left,count,pre)
#             if count == 0 and pre.val >= root.val:
#                 first = pre 
#                 count += 1 
#             if count == 1 and pre.val >= root.val:
#                 second = root 
#             pre = root 
#             inorder(root.right,count,pre)
            
#         inorder(root,0,pre)
#         first.val,second.val = second.val,first.val 