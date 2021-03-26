#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (51.62%)
# Likes:    417
# Dislikes: 0
# Total Accepted:    154.5K
# Total Submissions: 299.3K
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

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:#递归
        if not head or not head.next:
            return head   
        
        if head.next.val != head.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            p = head.next  
            while p.next and p.next.val == head.val:
                p = p.next 
            return self.deleteDuplicates(p)
        return head 
        

        
        # if head.val != head.next.val:
        #     head.next = self.deleteDuplicates(head.next)
        # else:
        #     p = head.next
        #     while p and p.val == head.val:
        #         p = p.next  
        #     return self.deleteDuplicates(p)
        # return head 

        

# @lc code=end

    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return head   
        
    #     dummy = ListNode()
    #     dummy.next = head   
        
    #     slow,fast = head,head.next  
        
    #     while fast:
    #         if slow.val != fast.val:
    #             slow.next = fast  
    #             slow = slow.next  
    #         fast = fast.next  
    #     slow.next = None  
        
    #     return head 
    
    
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return head   
        
        
    #     p1,p2 = head,head.next  
        
    #     while p2:
    #         if p1.val != p2.val:
    #             p1 = p1.next  
    #             p2 = p2.next  
    #         else:
    #             p2 = p2.next  
    #             p1.next = p2  
                
    #     p1.next = None  
    #     return head 
    
    
        # def deleteDuplicates(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head   
        
        # cur = head  
        
        # while cur and cur.next: 
        #     while cur.next and cur.val == cur.next.val:
        #         cur.next = cur.next.next  
        #     cur = cur.next  

        # return head 
        
    # def deleteDuplicates(self, head: ListNode) -> ListNode:#递归
    #     if not head or not head.next:
    #         return head   
        
    #     head.next = self.deleteDuplicates(head.next)
        
    #     return head  if head.val != head.next.val else head.next 