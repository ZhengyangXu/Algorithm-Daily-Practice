#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (66.22%)
# Likes:    561
# Dislikes: 0
# Total Accepted:    128.4K
# Total Submissions: 193.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
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
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  
        dummy = ListNode()
        dummy.next = head   
        prev = dummy
        
        while head and head.next:
            first = head 
            second = head.next  
            
            prev.next = second  
            first.next = second.next  
            second.next = first   
            
            prev = first   
            head = head.next  
        return dummy.next 
       
# @lc code=end

    # def swapPairs(self, head: ListNode) -> ListNode: 递归
    #     if not head or not head.next:
    #         return head 
        
    #     first = head 
    #     second = head.next 

    #     first.next = self.swapPairs(second.next) 
    #     second.next = first
        
    #     return second
### 常规思路:链表题目不管有没有用，首先创立一个哑结点，指向头结点。
### 两两交换的话，首先创立一个哑结点，dummy,指向头结点，用于返回最后的结果。在建立一个指向哑结点的指针，prev = dummy,
### prev 的作用是指向两节点交换之后的第一个节点。first指向head,second指向head.next，首先prev先指向second,
### 接着first指向second.next,最后second指向first。前两个节点翻转完毕，后续节点操作步骤一样，这时,prev变成原先的first，也就是
### 翻转后的第二个节点，head变成head.next，其实就是把递归表示出来。

###递归:首先是结束递归条件，就是head或者head.next没有值时，返回head
                                               