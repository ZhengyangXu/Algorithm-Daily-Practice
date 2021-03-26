'''
Author: your name
Date: 2021-01-29 16:15:21
LastEditTime: 2021-03-18 18:51:14
LastEditors: Please set LastEditors
# Description: In User Settings Edit
FilePath: \IOe:\代码练习\每日一刷\题源分类\LeetCode\LeetCode日刷\python\92.反转链表-ii.py
'''
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

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None  
        
        count = 1 
        dummy = ListNode(0)
        dummy.next = head  
        pre = dummy 
        while count < m:
            pre = pre.next 
            count += 1 
            
        cur = pre.next
        tail = cur   
        p1 = pre  
        pre = None 
        while count <= n:
            nex = cur.next  
            cur.next = pre  
            pre = cur 
            cur = nex 
            count += 1 
        p1.next = pre 
        tail.next = cur 

        
        return dummy.next  
            
            
        
# @lc code=end

#    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         if not head:
#             return None  
#         prev,cur = None,head 
#         while m > 1:
#             prev = cur
#             cur = cur.next 
#             m,n = m-1,n-1  
        
#         tail,con = cur,prev
#         while n:
#             third = cur.next 
#             cur.next = prev  
#             prev = cur  
#             cur = third
#             n -= 1    
#         if con:
#             con.next = prev
#         else:
#             head = prev 
        
#         tail.next = cur 
#         return head    


    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    #     if not head:
    #         return None  
        
    #     count = 1 
    #     dummy = ListNode(0)
    #     dummy.next = head  
    #     pre = dummy 
    #     while count < m:
    #         pre = pre.next 
    #         count += 1 
            
    #     cur = pre.next
    #     tail = cur   
        
    #     while cur and count <= n:
    #         nex = cur.next  
    #         cur.next = pre.next  
    #         pre.next = cur 
    #         tail.next = nex 
    #         cur = nex 
    #         count += 1 

        
    #     return dummy.next  
            