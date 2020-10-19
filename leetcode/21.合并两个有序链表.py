#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (62.95%)
# Likes:    1118
# Dislikes: 0
# Total Accepted:    295K
# Total Submissions: 468.6K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # recursion 
            if not l1:
                return l2 
            elif not l2:
                return l1 
            elif l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next,l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1,l2.next)
                return l2       
        

        
        
# @lc code=end

        '''迭代
        p = ListNode(-1)
        prev = p   
        
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1 
                l1 = l1.next 
            else:
                prev.next = l2 
                l2 = l2.next 
            prev = prev.next   
        
        if l1: prev.next = l1 
        if l2: prev.next = l2  
        return p.next''' 

