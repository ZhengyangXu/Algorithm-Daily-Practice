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
    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 迭代
        
    #     def reverse(head,tail):
    #         prev = tail.next 
    #         p = head  
    #         while prev != tail:
    #             nex = p.next 
    #             p.next = prev  
    #             prev = p  
    #             p = nex 
    #         return tail,head
        
    #     dummy = ListNode(0)
    #     dummy.next = head 
    #     pre = dummy
        
    #     while head:
            
    #         tail = pre  
    #         for _ in range(k):
    #             tail = tail.next 
    #             if not tail:
    #                 return dummy.next  
    #         nex = tail.next 
    #         head,tail = reverse(head,tail)
    #         pre.next = head  
    #         tail.next = nex 
    #         pre = tail 
    #         head = tail.next  
        
    #     return dummy.next 
    
    #   def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 栈
    #     dummy = ListNode(0)
    #     p = dummy  
    #     while True: 
    #         count = k  
    #         stack = []
    #         tmp = head  
    #         while count and tmp:
    #             stack.append(tmp)
    #             tmp = tmp.next  
    #             count -= 1  
                
    #         if count:
    #             p.next = head  
    #             break 
            
    #         while stack:
    #             p.next = stack.pop()
    #             p = p.next 
            
    #         p.next = tmp 
    #         head = tmp  
    #     return dummy.next  
        
    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 递归
    #     cur = head 
    #     count = 0 
    #     while cur and count != k:
    #         cur = cur.next  
    #         count += 1 
    #     if count == k:
    #         cur = self.reverseKGroup(cur,k)
    #         while count:
    #             tmp = head.next 
    #             head.next = cur  
    #             cur = head  
    #             head = tmp  
    #             count -= 1 
    #         head = cur  
    #     return head 
    
        # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 递归
        # cur = head 
        # count = 0 
        # while cur and count != k:
        #     cur = cur.next  
        #     count += 1 
        # if count == k:
        #     cur = self.reverseKGroup(cur,k)
        #     while count:
        #         tmp = head.next 
        #         head.next = cur  
        #         cur = head  
        #         head = tmp  
        #         count -= 1 
        #     head = cur  
        # return head 
        
        #     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 递归
        # def cal_len(head):
        #     p = head 
        #     l = 0 
        #     while p:
        #         l += 1 
        #         p = p.next 
        #         if l >= k:
        #             return True  
        #     return False 
        
        # def reverseK(head,k):
        #     prev,cur = None,head
        #     while k:
        #         nxt = cur.next  
        #         cur.next = prev  
        #         prev = cur  
        #         cur = nxt  
        #         k -= 1 
        #     return prev,cur
        
        # def dfs(head,k):
        #     if not cal_len(head):
        #         return head 
        #     prev,cur = reverseK(head,k)
        #     head.next = dfs(cur,k)
        #     return prev  
        
        # return dfs(head,k)
        #    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 递归
        
        # def reverse(a,b):
        #     prev = None
        #     cur = a  
        #     while cur != b:
        #         nex = cur.next 
        #         cur.next = prev  
        #         prev = cur  
        #         cur = nex 
        #     return prev
        
        # if not head:
        #      return head
        # a = b = head  
        # for i in range(k):
        #     if not b:
        #         return head  
        #     b = b.next    
        
        # newhead = reverse(a,b)
        # a.next  = self.reverseKGroup(b,k)
        # return newhead 
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:## 尾插法
        dummy = ListNode(0)
        dummy.next = head  
        pre = tail = dummy
        while True:
            count = k  
            while count and tail:
                count -= 1 
                tail = tail.next  
            if not tail:
                break 
            head = pre.next  
            while pre.next != tail:
                cur = pre.next  
                pre.next = cur.next 
                cur.next = tail.next 
                tail.next = cur  
            pre = head  
            tail = head  
        return dummy.next         
        

        

            
        
            
    