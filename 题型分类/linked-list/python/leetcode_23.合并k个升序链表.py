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
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode: ## 暴力解法 K个链表逐一找最小值 超时
        
    #     if not lists:
    #         return 
    #     size = len(lists)
         
    #     head = ListNode(0)
    #     tail = head 
        
    #     while True:
    #         minNode = ListNode(float('inf'))
    #         mini = -1
    #         for i in range(size):
    #             if not lists[i]:
    #                 continue 
    #             if lists[i].val < minNode.val:
    #                 minNode = lists[i]
    #                 mini = i 
    #         if mini == -1:
    #             break
    #         tail.next = minNode
    #         lists[mini] = lists[mini].next 
    #         tail = tail.next   
            
    #     return head.next 
    
    
    #     import heapq
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode: ## 使用最小堆优化k指针暴力解法
        
    #     if not lists:
    #         return 
        
    #     pq = []
    #     for i in range(len(lists)):
    #         if lists[i]:
    #             heapq.heappush(pq,(lists[i].val,i))
                
    #     head = ListNode(0)
    #     tail = head 
        
    #     while pq:
    #         val,index = heapq.heappop(pq)
    #         tail.next = ListNode(val)
    #         lists[index] = lists[index].next
    #         tail = tail.next  
    #         if lists[index]:
    #             heapq.heappush(pq,(lists[index].val,index))    
                
    #     return head.next 
    
    #     import heapq
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode: ## 使用最小堆优化k指针暴力解法
        
    #     if not lists:
    #         return 
        
    #     pq = []
    #     for i in range(len(lists)):
    #         if lists[i]:
    #             heapq.heappush(pq,(lists[i].val,i))
    #             lists[i] = lists[i].next 

                
    #     head = ListNode(0)
    #     tail = head 
        
    #     while pq:
    #         val,index = heapq.heappop(pq)
    #         tail.next = ListNode(val)
    #         tail = tail.next  
    #         if lists[index]:
    #             heapq.heappush(pq,(lists[index].val,index))  
    #             lists[index] = lists[index].next 

                
    #     return head.next 
    
        
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode: ## 两两合并 
        
    #     def merge2(l1,l2):
    #         if not l1 or not l2:
    #             return l2 if l2 else l1 
            
    #         head = ListNode(0)
    #         tail = head  
            
    #         while l1 and l2:
    #             if l1.val < l2.val:
    #                 tail.next = l1 
    #                 l1 = l1.next  
    #             else:
    #                 tail.next = l2 
    #                 l2 = l2.next 
    #             tail = tail.next
            
    #         if l1 or l2:
    #             tail.next = l1 if l1 else l2   
                
    #         return head.next   
    
    #     res = None
    #     for i in range(len(lists)):
    #         res = merge2(res,lists[i])
            
    #     return res 
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2(l1,l2):
            if not l1 or not l2:
                return l1 if l1 else l2 
            
            if l1.val < l2.val:
                l1.next = merge2(l1.next,l2)
                return l1  
            else:
                l2.next = merge2(l1,l2.next)
                return l2 
            
        # def merge(lists,l,r):  分治递归合并
        #     if l == r:
        #         return lists[l]
        #     if l>r:
        #         return 
            
        #     m = l+ (r-l)//2
        #     return merge2(merge(lists,l,m),merge(lists,m+1,r))
        # return merge(lists,0,len(lists)-1)
        
        size = len(lists)
        
        while size > 1:
            idx = 0 
            for i in range(0,size,2):
                
                if i == size - 1: 
                     
                    lists[idx] = lists[i]
                    idx += 1
                else:
                     
                    lists[idx] = merge2(lists[i],lists[i+1])
                    idx += 1
            size = idx 
        return lists[0] if lists else None

      
                
            
         
    
    
    
    
    
    

    