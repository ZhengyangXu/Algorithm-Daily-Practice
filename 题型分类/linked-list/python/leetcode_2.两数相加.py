#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (37.64%)
# Likes:    4515
# Dislikes: 0
# Total Accepted:    459K
# Total Submissions: 1.2M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
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
     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
         p1,p2 = l1,l2 
         carry = 0 
         node = ListNode(0)
         p = node
         while p1 or p2:
             x = p1.val if p1 else 0 
             y = p2.val if p2 else 0 
             sum = x + y + carry
             
             carry = sum//10
             node.next = ListNode(sum%10)
             node = node.next
             if p1:
                 p1 = p1.next 
             if p2:
                 p2 = p2.next
         if carry:
            node.next = ListNode(carry)
            
         return p.next
            
            
         
         
   