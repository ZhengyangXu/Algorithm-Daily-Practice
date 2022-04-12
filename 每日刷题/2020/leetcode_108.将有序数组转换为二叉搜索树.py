#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (74.50%)
# Likes:    655
# Dislikes: 0
# Total Accepted:    128.6K
# Total Submissions: 172.5K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定有序数组: [-10,-3,0,5,9],
# 
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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
# def buildTree(left,right): 递归
#     if left > right:
#         return  
    
#     mid = (left + right) >> 1 
#     root = TreeNode(nums[mid])
    
#     root.left = buildTree(left,mid-1)
#     root.right = buildTree(mid+1,right)
    
#     return root  

# return buildTree(0,len(nums)-1)  

    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode: ##迭代
    #     if len(nums) == 0:
    #         return 
    #     node = []
    #     left = []
    #     right = []
    #     root = TreeNode(0)
    #     node.append(root)
    #     left.append(0)
    #     right.append(len(nums)-1)
        
        
    #     while node:
    #         curNode = node.pop(0)
    #         l = left.pop(0)
    #         r = right.pop(0)
    #         mid = l+(r-l)//2  
            
    #         curNode.val = nums[mid]
            
    #         if l <= mid-1:
    #             curNode.left = TreeNode(0)
    #             node.append(curNode.left)
    #             left.append(l)
    #             right.append(mid-1)
                
    #         if r >= mid+1:
    #             curNode.right = TreeNode(0)
    #             node.append(curNode.right)
    #             left.append(mid+1)
    #             right.append(r)
    #     return root  
    
    #    def sortedArrayToBST(self, nums: List[int]) -> TreeNode: ##迭代
    #     if len(nums) == 0:
    #         return  
        
        
        
    #     start,end = 0,len(nums)
        
    #     mid = (start+end)>>1
        
    #     root = (TreeNode(nums[mid]),start,end)  
        
    #     node = []
        
    #     node.append(root)
        
    #     while end - start > 1 or node:
            
    #         while end - start > 1:
    #             curRoot,start,end = node.pop() 
    #             mid = (start+end)>>1  
    #             end = mid  
    #             mid = (start+end)>>1
    #             curRoot.left = TreeNode(nums[mid])
    #             curRoot = curRoot.left  
    #             node.append((curRoot,start,end))
                
    #         curRoot,start,end = node.pop()
    #         mid = (start+end)>>1 
            
    #         start = mid + 1 
            
    #         if start < end:
    #             mid = (start+end)>>1  
    #             curRoot.right = TreeNode(nums[mid])
    #             curRoot = curRoot.right  
    #             node.append((curRoot,start,end))
                
    #     return root[0] 
        # def sortedArrayToBST(self, nums: List[int]) -> TreeNode: ##迭代
        # if len(nums) == 0:
        #     return  
        
        # nodes = []
        # lr = []
        
        # root = TreeNode(0)
        # nodes.append(root)
        
        # lr = [(0,len(nums)-1)]
        
        # while nodes:
        #     node = nodes.pop()
        #     start,end = lr.pop()
        #     mid = (start+end)>>1
        #     node.val = nums[mid]
            
        #     if start <= mid-1:
        #         node.left = TreeNode(0)
        #         nodes.append(node.left) 
        #         lr.append((start,mid-1))
                
                
        #     if end >= mid + 1:
        #         node.right = TreeNode(0)
        #         nodes.append(node.right)
        #         lr.append((mid+1,end))
                
        # return root  
                              
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode: ##迭代
        if len(nums) == 0:
            return 
        
        start,end = 0,len(nums)-1  
        root = TreeNode(0)
        
        stack = []
        stack.append((root,start,end))
        
        
        while stack:
            node,start,end = stack.pop()
            mid = (start+end)//2  
            node.val = nums[mid]
            
            if start <= mid-1:
                node.left = TreeNode(0)
                stack.append((node.left,start,mid-1))
                
            if end >= mid+1:
                node.right = TreeNode(0)
                stack.append((node.right,mid+1,end))
                
        return root          
    