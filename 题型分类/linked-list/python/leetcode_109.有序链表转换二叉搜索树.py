# @before-stub-for-debug-begin

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (73.02%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    35.4K
# Total Submissions: 48.4K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定的有序链表： [-10, -3, 0, 5, 9],
# 
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    # def sortedListToBST(self, head: ListNode) -> TreeNode:
    #     if not head:
    #         return 
    #     if not head.next:
    #         return TreeNode(head.val)
        
    #     def getMedian(left,right):
            
    #         slow = fast = left  
            
    #         while fast != right  and fast.next != right:
    #             fast = fast.next.next  
    #             slow = slow.next  
    #         return slow  
        
    #     def buildTree(left,right):
    #         if left == right:
    #             return  
            
    #         mid = getMedian(left,right)
    #         root = TreeNode(mid.val)
            
    #         root.left = buildTree(left,mid)
    #         root.right = buildTree(mid.next,right)
            
    #         return root   
        
    #     return buildTree(head,None)
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        def getLength(head):
            ret = 0 
            while head:
                ret += 1 
                head = head.next  
            return ret   
        
        def buildTree(left,right):
            if left > right:
                return  
            mid = (left+right+1)//2  
            
            root = TreeNode()
            
            root.left = buildTree(left,mid-1)
            
            nonlocal head  
            
            root.val = head.val 
            head = head.next  
            root.right = buildTree(mid+1,right)
            return root  
        length = getLength(head)
        return buildTree(0,length-1)
            
            
            
         
        
    