#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#
# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (66.47%)
# Likes:    313
# Dislikes: 0
# Total Accepted:    82.9K
# Total Submissions: 124.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
# 
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
# 
# 计算从根到叶子节点生成的所有数字之和。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
# 
# 示例 2:
# 
# 输入: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
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
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(root,pretotal):
            if not root:
                return 0 
            total = pretotal * 10 + root.val 
            if not root.left and not root.right:
                return total 

            else:
                return dfs(root.left,total) + dfs(root.right,total)

        
        dfs(root,0)
        
        return dfs(root,0)
                
# @lc code=end

    #  def sumNumbers(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     res = []
    #     def dfs(root,path):
    #         if not root:
    #             return  
            
    #         if not root.left and not root.right:
    #             res.append(path)
    #             return 
                
    #         dfs(root.left,path+str(root.left.val) if root.left else '')
    #         dfs(root.right,path+str(root.right.val) if root.right else '')
    #         path = path[:len(path)-1]
        
    #     dfs(root,str(root.val))
        
    #     ans = 0
    #     for num in res:
    #         ans += int(num)
            
    #     return ans
                