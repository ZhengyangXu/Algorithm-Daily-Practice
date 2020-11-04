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
        dummy = ListNode(0)
        dummy.next = head   
        
        slow,fast = dummy,head  
        
        for i in range(n):
            fast = fast.next 
        
        while fast:
            slow = slow.next  
            fast = fast.next 
            
        dn = slow.next 
        slow.next = dn.next 
        #dn.next = None     
        
        return dummy.next
        

            
# @lc code=end
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode: 两次遍历
    #     dummy = ListNode(0)
    #     dummy.next = head 
    #     p1,p2 = head,dummy
    #     count = 0    
    #     while p1:
    #         count += 1 
    #         p1 = p1.next
    #     length = count - n   
    #     while length > 0:
    #         length -= 1 
    #         p2 = p2.next 
    #     p2.next = p2.next.next 
        
    #     return dummy.next  


