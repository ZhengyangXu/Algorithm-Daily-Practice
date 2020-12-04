#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (62.09%)
# Likes:    647
# Dislikes: 0
# Total Accepted:    85.6K
# Total Submissions: 137.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 
# 
# 示例：
# 
# 给你这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 
# 
# 说明：
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 递归  
        
        if not head or not head.next:
            return head  
        cur = head  
        count = 0 
        while cur and count != k:
            cur = cur.next 
            count += 1 
        
        if count == k:
            cur = self.reverseKGroup(cur,k)
            while count: 
                tmp = head.next  
                head.next = cur   
                cur = head   
                head = tmp   
                count -= 1 
            
            head = cur  
        return head  

            
# @lc code=end

#   def reverseKGroup(self, head: ListNode, k: int) -> ListNode:  ## 按段翻转    
#         def reverse(head,tail):
#             prev = ListNode()
#             prev.next = head    
#             p = head  
            
#             while prev != tail:
#                 nex = p.next  
#                 p.next = prev  
#                 prev = p   
#                 p = nex 
#             return tail,head 
        
        
        
#         dummy = ListNode()
#         dummy.next = head   
#         prev = dummy  
        
#         while head:
#             tail = prev    
#             for i in range(k):
#                 tail = tail.next  
#                 if not tail:
#                     return dummy.next    
            
#             nex = tail.next 
#             head,tail = reverse(head,tail)
#             prev.next = head  
#             tail.next = nex
#             prev = tail
            
#             head = tail.next  
#         return dummy.next 















    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 栈
        
    #     if not head or not head.next:
    #         return head  
    #     dummy = ListNode()
    #     dummy.next = head  
    #     p = dummy  
        
    #     while True: 
    #         stack = []
    #         count = k  
    #         tmp = head   
    #         while count and tmp:
    #             stack.append(tmp)
    #             tmp = tmp.next  
    #             count -= 1 
    #         if count: 
    #             return dummy.next    
            
    #         while stack: 
    #             p.next = stack.pop()
    #             p = p.next   
                
    #         p.next = tmp   
    #         head = tmp   
    #     return dummy.next  
    
    
    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 尾插？？
        
        # if not head or not head.next:
        #     return head  
        
        # dummy = ListNode()
        # dummy.next = head  
        # prev = dummy    
        
        # while True:   
        #     tail = prev  
        #     count = k  
        #     while count and tail:
        #         tail = tail.next   
        #         count -= 1 
        #     if not tail:
        #         return dummy.next  
        #     head = prev.next 
        #     while prev.next != tail:
        #         cur = prev.next  
        #         prev.next = cur.next 
        #         cur.next = tail.next  
        #         tail.next = cur  
        #     prev = head  
        
        # return dummy.next 