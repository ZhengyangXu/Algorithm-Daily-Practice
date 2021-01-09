# 面试题16：反转链表

# 题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。链表结点定义如下：
class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None 

def reverseLinkedList(head): ## 迭代
    if not head or not head.next:
        return head 

    pre,cur = None,head 
    
    while cur:
        nex = cur.next 
        cur.next = pre 
        pre = cur 
        cur = nex
    
    return pre
def reverse(head):##递归
    if not head or not head.next:
        return head
    
    newhead = reverse(head.next)
    head.next.next = head 
    head.next = None 
    
    return newhead 

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    
    head = reverseLinkedList(node1)
    head2 = reverse(node1)
    # print(head.val)
    # print(head.next.val)
    while head:
        print(head.val)
        head = head.next 

    