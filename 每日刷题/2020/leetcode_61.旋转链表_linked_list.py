#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (40.52%)
# Likes:    380
# Dislikes: 0
# Total Accepted:    101.6K
# Total Submissions: 250.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 
# 
# 示例 2:
# 
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def rotateRight(self, head: ListNode, k: int) -> ListNode:  模拟法
#     if not head or not head.next:
#         return head  
    
#     dummy = ListNode()
#     dummy.next = head   
    
#     cur = dummy  
#     count = 0 
    
#     while cur.next:
#         count += 1 
#         cur = cur.next    
        
#     k %= count  
    
#     if k == 0:
#         return head  
    
#     tail = head
#     for _ in range(count - k -1):
#         tail = tail.next  
        
#     newtail,newhead = tail,tail.next   
    
#     cur.next = head  
#     newtail.next = None  
    
#     return newhead  
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:#链表成环
        if not head or not head.next:
            return head  
        
        dummy = ListNode()
        dummy.next = head   
        
        cur = dummy  
        count = 0 
        
        while cur.next:
            count += 1 
            cur = cur.next    
            
        cur.next = head  ## 成环  
        
        k %= count
          
        tail = head
        for _ in range(count - k -1):
            tail = tail.next  
            
        newhead = tail.next  
        tail.next = None  
        
        return newhead  
        
            
 
            
            
            
            
        
    