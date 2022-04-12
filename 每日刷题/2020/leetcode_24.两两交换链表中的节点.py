#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (66.22%)
# Likes:    561
# Dislikes: 0
# Total Accepted:    128.4K
# Total Submissions: 193.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    # def swapPairs(self, head: ListNode) -> ListNode:## 迭代
    #     if not head or not head.next:
    #         return head  
    #     dummy = ListNode(0)
    #     dummy.next = head  
    #     prev = dummy
        
    #     while head and head.next:
    #         first = head 
    #         second = head.next 
            
    #         prev.next = second 
    #         first.next = second.next  
    #         second.next = first  
            
    #         prev = first  
    #         head = head.next  
            
    #     return dummy.next 
    
    
    # def swapPairs(self, head: ListNode) -> ListNode:## 直接交换节点值
    #     if not head or not head.next:
    #         return head  
    #     dummy = ListNode(0)
    #     dummy.next = head  
    #     prev = dummy
        
    #     while head and head.next:
    #         first = head 
    #         second = head.next 
            
    #         first.val,second.val = second.val,first.val 
            
    #         head = second.next 
            
    #     return dummy.next 
    
        # def swapPairs(self, head: ListNode) -> ListNode:## 递归
        # if not head or not head.next:
        #     return head  
        
        
        # first = head  
        # second = head.next  
        
        # first.next = self.swapPairs(second.next)
        # second.next = first 
        
        
        
        
        
        # return second
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:## 递归
        if not head or not head.next:
            return head  
        
        
        
        temp = head.next  
        
        head.next = self.swapPairs(head.next.next)
        
        temp.next = head
        
        
        
        
        
        return temp
            
            
        
    