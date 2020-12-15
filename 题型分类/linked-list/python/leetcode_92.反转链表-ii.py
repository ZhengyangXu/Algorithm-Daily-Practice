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

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#     if not head or not head.next or m == n:
#         return head   
    
#     dummy = ListNode()
#     dummy.next = head  
#     prev,cur = dummy,head   
#     count = 1
#     while cur and cur.next:
#         if count != m:
#             cur = cur.next
#             prev = prev.next
#             count += 1    
#         else:
#             prev2 = prev.next  
#             cur2 = cur.next 
#             while cur2 and m != n: 
#                 nex = cur2.next  
#                 cur2.next = prev2 
#                 prev2 =cur2  
#                 cur2 = nex 
#                 m += 1 
#             cur.next = cur2 
#             prev.next = prev2  
#             break  
#     return dummy.next 

    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
    #     def reverseN(head,n,successor):
    #         if n == 1:
    #             successor = head.next 
    #             return head  
            
    #         last = reverseN(head,n-1,successor)
    #         head.next.next = head  
            
    #         head.next = successor
    #         return last 
        
    #     if m == 1:
    #         return reverseN(head,n,ListNode())
        
    #     head.next = self.reverseBetween(head.next,m-1,n-1)
        
    #     return head  
             
        # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # if not head:
        #     return None  
        
        # left,right = head,head  
        # stop = False  
        
        # def reverseMN(right,m,n):
        #     nonlocal left,stop
            
        #     if n == 1:
        #         return  
            
        #     right =right.next  
            
        #     if m > 1:
        #         left = left.next  
                
        #     reverseMN(right,m-1,n-1)
            
        #     if left == right or right.next == left:
        #         stop = True  
                
        #     if not stop:
        #         left.val,right.val = right.val,left.val 
        #         left = left.next  
            
        # reverseMN(right,m,n)
        # return head 
    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
    #     def reverseN(head,n):
    #         if n == 1:
    #             return head 
            
    #         last = reverseN(head.next,n-1)
            
    #         successor = head.next.next 
    #         head.next.next = head  
    #         head.next = successor  
    #         return last 
        
    #     if m == 1:
    #         return reverseN(head,n)
        
    #     head.next = self.reverseBetween(head.next,m-1,n-1)
        
    #     return head 
        
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        def reverseN(head,n):
            if n == 1:
                successor = head.next
                return head,successor  
            
            last,successor = reverseN(head.next,n-1)
            
            
            head.next.next = head  
            head.next = successor  
            return last,successor  
        
        if m == 1:
            last,_ = reverseN(head,n)
            return last
        
        head.next = self.reverseBetween(head.next,m-1,n-1)
        
        return head 
        
