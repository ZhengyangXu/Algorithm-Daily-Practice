#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (43.16%)
# Likes:    758
# Dislikes: 0
# Total Accepted:    81.2K
# Total Submissions: 188K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
# 
# 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 输出：6
# 
# 
# 示例 2：
# 
# 输入：[-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# 输出：42
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
    def __init__(self):
        self.ans = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        
        def helper(root):
            if not root:
                return 0  
            left = max(0,helper(root.left))
            right = max(0,helper(root.right))
            self.ans = max(self.ans,root.val+left+right)
            return root.val + max(left,right)
        helper(root)
        
        return self.ans
            
            
        
        
# @lc code=end

## 思路：递归。一定要记住自己的递归函数是干嘛用的，不要跳到递归的内部实现中去。
## 比如这道题，递归函数的作用是返回当前路径的最大值，那么站在root的角度来说，
## 就是用root的值加上左子树的最大路径值，再加上右子树的最大路径值。这里返回的
## 值要注意，如果子树同时存在左右两个节点，那么应该去两个节点中的max+当前节点的
## 值作为返回值，因为路径不包含分支，比如例子中[-10,20,15,7],不存在这样的路径