#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (60.30%)
# Likes:    286
# Dislikes: 0
# Total Accepted:    61.5K
# Total Submissions: 102K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 
# 你应当保留两个分区中每个节点的初始相对位置。
# 
# 
# 
# 示例:
# 
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        dummy1 = ListNode()
        dummy2 = ListNode()
        p1,p2 = dummy1,dummy2   
        cur = head  
        while cur:
            if cur.val < x:
                p1.next = cur  
                p1 = p1.next  
            else:
                p2.next = cur  
                p2 = p2.next  
            cur = cur.next if cur else None  

        p2.next = None 
        p1.next = dummy2.next 
        return dummy1.next  
        
# @lc code=end

