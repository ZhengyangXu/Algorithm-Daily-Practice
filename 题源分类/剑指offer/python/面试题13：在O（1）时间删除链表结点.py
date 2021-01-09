# 面试题13：在O（1）时间删除链表结点
# 题目：给定单向链表的头指针和一个结点指针，定义一个函数在 O（1）时间删除该结点。链表结点与函数的定义如下：

class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None 

def deleteNode(head,target):
    if not head or not target:
        return 
    dummy = Node(0)
    dummy.next = head
    if head == target:
        return 
    if target.next:
        next = target.next 
        target.value = next.value 
        target.next = next.next 
        del next 
    else:
        while head:
            if head.next == target:
                head.next = None 
            head = head.next
    return dummy.next

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    p = deleteNode(node1,node4)
    
    while p:
        print(p.val)
        p = p.next  