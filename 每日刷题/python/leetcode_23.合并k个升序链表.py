#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (51.97%)
# Likes:    725
# Dislikes: 0
# Total Accepted:    132.3K
# Total Submissions: 254.7K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode: ##k指针排列
    #     if not lists:
    #         return 
    #     head = ListNode(0)
    #     tail = head
    #     while True:
    #         minNode = None 
    #         minindex = -1 
    #         for i in range(len(lists)):
    #             if not lists[i]:
    #                 continue  
    #             if not minNode or lists[i].val < minNode.val:
    #                 minNode = lists[i]
    #                 minindex = i
    #         if minindex == -1:
    #             break 
    #         tail.next = minNode 
    #         tail = tail.next 
  
    #         lists[minindex] = lists[minindex].next 
                 
        
    #     return head.next 
    
    #     import heapq
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode: ##最小堆

    #     que = []
        
    #     size = len(lists)
        
    #     for i in range(size):
    #         if lists[i]:
    #             heapq.heappush(que,(lists[i].val,i))
    #     head = ListNode(0)
    #     tail = head      
    #     while que:
    #         minval,minindex = heapq.heappop(que)
    #         tail.next = ListNode(minval)
    #         tail = tail.next
    #         lists[minindex] = lists[minindex].next
    #         if lists[minindex]:
    #             heapq.heappush(que,(lists[minindex].val,minindex))
        
    #     return head.next 
class Solution:
    import heapq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode: ##分治
        def mergeRecur(l1,l2):##迭代
            if not l1 and not l2:
                return 
            if not l1 or not l2:
                return l1 if l1 else l2 
            
            if l1.val < l2.val:
                l1.next = mergeRecur(l1.next,l2)
                return l1
            else:
                l2.next = mergeRecur(l1,l2.next)
                return l2
        def mergeIte(l1,l2):
            if not l2 or not l1:
                return l1 if l1 else l2 
            
            head = ListNode(0)
            tail = head  
            
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1 
                    l1 = l1.next 
                else:
                    tail.next = l2 
                    l2 = l2.next 
                tail = tail.next
            if l1 or l2:
                tail.next = l1 if l1 else l2
            return head.next  
        
        def merge(lists,l,r):
            if l == r:
                return lists[l]
            if l > r:
                return 
            m = l + (r-l)//2  
            # return mergeRecur(merge(lists,l,m),merge(lists,m+1,r))
            return mergeIte(merge(lists,l,m),merge(lists,m+1,r))
        res = None 
        for i in range(len(lists)):
            res = mergeRecur(res,lists[i])
            
        # return merge(lists,0,len(lists)-1)     
        return res    

            

    