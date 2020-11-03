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

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode: ##双指针
        
        if not head:
            return 
        
        slow,fast = head,head.next
        
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next 
            fast = fast.next  
        slow.next = None 
        return head  
                

            
# @lc code=end

    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     current = head 
    #     while current and current.next:
    #         if current.val == current.next.val:
    #             current.next = current.next.next 
    #         else:
    #             current = current.next 
    #     return head 