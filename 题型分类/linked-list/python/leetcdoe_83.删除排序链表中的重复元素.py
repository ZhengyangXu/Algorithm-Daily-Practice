#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (50.96%)
# Likes:    358
# Dislikes: 0
# Total Accepted:    123.5K
# Total Submissions: 242K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    # def deleteDuplicates(self, head: ListNode) -> ListNode: ##双指针
    #     if not head or not head.next:
    #         return head  
        
    #     cur,nex = head,head.next  
        
    #     while nex:
    #         if cur.val != nex.val:
    #             cur = cur.next   
    #             nex = nex.next  
    #         else:
    #             nex = nex.next  
    #             cur.next = nex  
    #     cur.next = None
    #     return head  
        # def deleteDuplicates(self, head: ListNode) -> ListNode: ##双指针
        # if not head or not head.next:
        #     return head  
        
        # p1,p2 = head,head.next  
        
        # while p2:
        #     if p1.val != p2.val:
        #         p1.next = p2  
        #         p1 = p1.next 
        #     p2 = p2.next  
        # p1.next = None  
        
        # return head 
        # def deleteDuplicates(self, head: ListNode) -> ListNode: ##双指针
        # if not head or not head.next:
        #     return head  
        
        # cur = head  
        
        # while cur and cur.next:
        #     if cur.val == cur.next.val:
        #         cur.next = cur.next.next  
        #     else:
        #         cur = cur.next   
        # return head  
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode: ##双指针
        if not head or not head.next:
            return head  
        
        cur = head  
        
        while cur and cur.next:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next  
            cur = cur.next  
        return head 
 
        

            
        