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


    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 递归 
    #     cur,count = head,k 
        
    #     while cur and count:
    #         cur = cur.next 
    #         count -= 1 
    #     if count == 0:
    #         cur = self.reverseKGroup(cur,k)
    #         while k:
    #             nex = head.next  
    #             head.next = cur  
    #             cur = head  
    #             head = nex 
    #             k -= 1 
                
    #         head = cur  
    #     return head 
    
    
        # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 递归
        # def reverse(head,k):
        #     cur,prev = head,None 
        #     while k:
        #         nex = cur.next  
        #         cur.next = prev  
                
        #         prev = cur  
        #         cur = nex 
        #         k -= 1 
        #     return prev,head  
        
        # if not head:
        #     return head  
        
        # cur = head  
        # for _ in range(k):
        #     if not cur: 
        #         return head 
        #     cur = cur.next   
            
        # newhead = reverse(head,k)
        # head.next = self.reverseKGroup(cur.next,k)
        
        # return newhead 
        
        
        #     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 栈
        
        # if not head or not head.next:
        #     return head  
        
        # stack = []
        
        # dummy = ListNode(0)
        # p = dummy  
        # while True:  
        #     count = k  
        #     cur = head  
            
        #     while count and cur:
        #         stack.append(cur)
        #         cur = cur.next   
        #         count -= 1 
        #     if count:
        #         p.next = head  
        #         break 
        #     while stack:
        #         p.next = stack.pop()
        #         p = p.next
                
        #     p.next = cur  
        #     head = cur   
        # return dummy.next  
        
        #     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 尾插法
        # dummy = ListNode(0)
        # dummy.next = head  
        # prev,tail = dummy,head   
        # while True:
        #     count = 0 
        #     while tail and count != k-1:
        #         tail = tail.next  
        #         count += 1
                
        #     if not tail:
        #         break  
        #     head = prev.next  
        #     while prev.next != tail:
        #         cur = prev.next  
        #         prev.next = cur.next  
        #         cur.next = tail.next 
        #         tail.next = cur  
                
        #     prev = head  
        #     tail = prev.next 
            
        # return dummy.next 
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 迭代 
        

                


            

                
                
            
            

            

            
                   
    