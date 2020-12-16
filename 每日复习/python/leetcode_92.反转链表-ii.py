#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (50.41%)
# Likes:    403
# Dislikes: 0
# Total Accepted:    56.6K
# Total Submissions: 112.3K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#


#     def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         if not head:
#             return None  
#         prev,cur = None,head  
        
#         while m > 1:
#             prev = cur  
#             cur = cur.next  
#             m -= 1
#             n -= 1  
            
#         tail,con = cur,prev
        
#         while n:
#             nex = cur.next  
#             cur.next = prev  
#             prev = cur  
#             cur = nex  
#             n -= 1 
            
#         if con:
#             con.next = prev  
#         else:
#             head = prev 
        
#         tail.next = cur  
        
#         return head   


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x

    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
    #     if not head or not head.next:
    #         return head  
        
    #     def reverseN(head,n):
    #         if n == 1:
    #             successor = head.next  
    #             return head,successor   
            
    #         last,successor = reverseN(head.next,n-1)
    #         head.next.next = head  
    #         head.next = successor  
            
    #         return last,successor  
        
    #     if m == 1:
    #         last,_ = reverseN(head,n)
    #         return last  
        
    #     head.next = self.reverseBetween(head.next,m-1,n-1)
        
    #     return head  
                
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if not head or not head.next:
            return head  
        
        def reverseN(head,n):
            if n == 1: 
                return head 
            
            last = reverseN(head.next,n-1)
            
            successor = head.next.next
            
            head.next.next = head  
            
            head.next = successor  
            
            return last   
        
        if m == 1:
            return reverseN(head,n) 
        
        head.next = self.reverseBetween(head.next,m-1,n-1)
        
        return head  
                
        
