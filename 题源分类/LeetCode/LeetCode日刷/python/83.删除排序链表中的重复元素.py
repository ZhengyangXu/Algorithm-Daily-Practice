
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
    