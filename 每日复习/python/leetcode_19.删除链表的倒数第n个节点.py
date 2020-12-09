#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (39.33%)
# Likes:    983
# Dislikes: 0
# Total Accepted:    230.6K
# Total Submissions: 585.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:#一次遍历
        # if not head:
        #     return 
        # dummy = ListNode(0)
        # dummy.next = head 
        # slow,fast = dummy,head  
        # for _ in range(n):
        #     fast = fast.next  
        
        # while fast:
        #     fast = fast.next
        #     slow = slow.next  
        
        # slow.next = slow.next.next  
        # return dummy.next 
        
        if not head:
            return  
        dummy = ListNode(0)
        dummy.next = head
        cur1,cur2 = head,dummy
        size = 0 
        while cur1:
            size += 1 
            cur1 = cur1.next 
            
        length = size - n  
        while length > 0:
            length -= 1
            cur2 = cur2.next 
        cur2.next = cur2.next.next  
        return dummy.next 
            
    