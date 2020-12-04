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

class Solution:
    import heapq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode: ## 最小堆 优先队列 
        head = []
        dummy = ListNode()
        p = dummy   
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head,(lists[i].val,i))
                lists[i] = lists[i].next  
        while head:
            val,index = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next  
            if lists[index]:
                heapq.heappush(head,(lists[index].val,index))
                lists[index] = lists[index].next  
        return dummy.next  
                
# @lc code=end
#def mergeKLists(self, lists: List[ListNode]) -> ListNode: ## 递归+分治
   

#   def merge2(a,b):  递归和并
#             if not a or not b:
#                 return a if a else b 
#             head = ListNode()
#             tail = head 
#             pa,pb = a,b  
#             while pa and pb:
#                 if pa.val < pb.val:
#                     tail.next = pa  
#                     pa = pa.next  
#                 else:
#                     tail.next = pb  
#                     pb = pb.next  
#                 tail = tail.next   
#             if pa:
#                 tail.next = pa  
#             if pb: 
#                 tail.next = pb
#             return head.next    
#         def merge(lists,l,r):
#             if l == r:
#                 return lists[l]
#             if l > r:
#                 return 
#             m = l + (r-l)//2
#             return merge2(merge(lists,l,m),merge(lists,m+1,r))
        
#         return merge(lists,0,len(lists)-1)




#   def mergeKLists(self, lists: List[ListNode]) -> ListNode: ## 递归分治
#         def mergetwo(l1,l2):
#             if not l1 or not l2:
#                 return l1 if l1 else l2  
#             if l1.val < l2.val:
#                 l1.next = mergetwo(l1.next,l2)
#                 return l1
#             else:
#                 l2.next = mergetwo(l1,l2.next)
#                 return l2   
#         def merge(lists,l,r):
#             if l == r:
#                 return lists[l]
#             if l > r:
#                 return  
#             m = l + (r-l)//2
#             return mergetwo(merge(lists,l,m),merge(lists,m+1,r))
#         if not list:
#             return 
#         return merge(lists,0,len(lists)-1)