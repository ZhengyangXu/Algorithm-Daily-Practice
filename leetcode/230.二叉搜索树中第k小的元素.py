#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (72.26%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    75.1K
# Total Submissions: 103.9K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
# 
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
# 
# 示例 1:
# 
# 输入: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# 输出: 1
# 
# 示例 2:
# 
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# 输出: 3
# 
# 进阶：
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
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
    def kthSmallest(self, root: TreeNode, k: int) -> int: ##迭代
        
        if not root or not k:
            return  
        
        stack = []
        node = root  
        count = 0 
        
        while stack or node:
            if node:
                while node:
                    stack.append(node)
                    node = node.left  
            else:
                node = stack.pop()
                count += 1 
                if count == k:
                    return node.val  
                node = node.right 
                
        
            
            
            
            
            
        
# @lc code=end

    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     if not root or not k:
    #         return 
    #     ans = []
    #     def midorder(root):
    #         if not root:
    #             return  
            
    #         midorder(root.left)
    #         ans.append(root.val)
    #         midorder(root.right)
        
    #     midorder(root)
        
    #     return ans[k-1]


## 思路：直接中序遍历加入到数组，取第k个最小的值，需要遍历完整棵树才行，实现比较差

#  def kthSmallest(self, root: TreeNode, k: int) -> int: 递归
#         if not root or not k:
#             return 
#         count = 0 
#         res = 0 
         
#         def midorder(root,k):
#             if not root:
#                 return  
#             nonlocal count,res 
#             midorder(root.left,k)
#             count += 1 
#             if count == k:
#                 res = root.val
#                 return 
#             midorder(root.right,k)
        
#         midorder(root,k)
#         return res  