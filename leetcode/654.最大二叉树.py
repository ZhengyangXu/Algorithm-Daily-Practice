#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#
# https://leetcode-cn.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (81.60%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    23K
# Total Submissions: 28.2K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
# 
# 
# 二叉树的根是数组中的最大元素。
# 左子树是通过数组中最大值左边部分构造出的最大二叉树。
# 右子树是通过数组中最大值右边部分构造出的最大二叉树。
# 
# 
# 通过给定的数组构建最大二叉树，并且输出这个树的根节点。
# 
# 
# 
# 示例 ：
# 
# 输入：[3,2,1,6,0,5]
# 输出：返回下面这棵树的根节点：
# 
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    / 
# ⁠    2  0   
# ⁠      \
# ⁠       1
# 
# 
# 
# 
# 提示：
# 
# 
# 给定的数组的大小在 [1, 1000] 之间。
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode: ##单调栈
        
        if len(nums) == 0:
            return 
        
        stack = [TreeNode(nums[0])]
        
        for i in range(1,len(nums)):
            cur_node = TreeNode(nums[i])
            if cur_node.val < stack[-1].val:
                stack.append(cur_node)
            else:
                while stack and stack[-1].val < cur_node.val:
                    node = stack.pop() 
                    if stack:
                        if stack[-1].val < cur_node.val:
                            stack[-1].right = node   
                        else: 
                            cur_node.left = node  
                    else:
                        cur_node.left = node  
                stack.append(cur_node)
        if stack:
            top = stack[0]
            for i in range(len(stack)-1):
                stack[i].right = stack[i+1]
        
        return top               
# @lc code=end

#  def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode: ## 递归
        
#         def build(nums,low,high):
            
#             if low > high:
#                 return   
            
#             indx,maxvalue = -1,float("-inf")
            
#             for i in range(low,high+1):
#                 if nums[i] >= maxvalue:
#                     maxvalue = nums[i]
#                     indx = i    
            
#             root = TreeNode(maxvalue)
#             root.left = build(nums,low,indx-1)
#             root.right = build(nums,indx+1,high)
            
#             return root   
        
#         return build(nums,0,len(nums)-1)
            