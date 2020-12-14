#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (48.49%)
# Likes:    328
# Dislikes: 0
# Total Accepted:    57.1K
# Total Submissions: 117.6K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# 
# 示例 1:
# 
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
# 
# 示例 2:
# 
# 输入: 1->1->1->2->3
# 输出: 2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  
        
        dummy = ListNode(float('inf'))
        dummy.next = head  
        slow,fast = dummy,head.next  
        
        while fast:
            if slow.next.val != fast.val:
                slow = slow.next  
                fast = fast.next  
            else:
                while fast and slow.next.val == fast.val:
                    fast = fast.next  
                    
                slow.next = fast    
                fast = fast.next  if fast else None 
                
        return dummy.next 
    