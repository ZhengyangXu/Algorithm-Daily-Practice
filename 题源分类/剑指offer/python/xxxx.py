# 面试题17：合并两个排序的链表
# 题目：输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按照递增排序的。
# 例如输入图3.7中的链表1和链表2，则合并之后的升序链表如链表3所示。链表结点定义如下：
class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None 


def merge2(l1,l2): ## 迭代
    if not l1 or not l2:
        return l1 if not l2 else l2 
    
    p1,p2 = l1,l2 
    dummy = Node(-1)
    p = dummy 
    while p1 and p2:
        if p1.val <= p2.val:
            p.next = p1  
            p1 = p1.next 
        else:
            p.next = p2  
            p2 = p2.next 
        p = p.next  
    
    if p1:
        p.next = p1 
    if p2:
        p.next = p2 
        
    return dummy.next 

def mergeRec(l1,l2):## 递归
    
    if not l1 or not l2:
        return l1 if not l2 else l2 
    

    if l1.val <= l2.val:
        l1.next = mergeRec(l1.next,l2)
        return l1 
    else:
        l2.next = mergeRec(l1,l2.next)
        return l2 
            
   


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node3
    node2.next = node4
    node3.next = node5
    node4.next = node6
    
    # head = merge2(node1,node2)
    head = mergeRec(node1,node2)
    while head:
        print(head.val)
        head = head.next 