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
                
## 思路：和数组一样的思路。判断快指针和慢指针或者指定的值的值，如果相等，则fast = fast.next,
## 否则，slow.next指向fast，同时更新slow为slow.next.fast指针一直向前走，套路是慢指针不判断，
## 跟随快指针的判断结果改变
            
# @lc code=end

    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     current = head 
    #     while current and current.next:
    #         if current.val == current.next.val:
    #             current.next = current.next.next 
    #         else:
    #             current = current.next 
    #     return head 
    