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
    ans = float("-inf")
    def maxPathSum(self, root: TreeNode) -> int:
        

        def helper(root):
            if not root:
                return 0  
            left = max(0,self.maxPathSum(root.left))
            right = max(0,self.maxPathSum(root.right))
            ans = max(ans,root.val+left+right)
            return max(left,right)+root.val
        helper(root)
        return ans
        
        
# @lc code=end

