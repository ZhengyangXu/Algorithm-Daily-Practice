# 面试题26：复杂链表的复制
# 题目：请实现函数ComplexListNode*Clone（ComplexListNode*pHead），
# 复制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个结点外，
# 还有一个m_pSibling 指向链表中的任意结点或者NULL。结点的C++定义如下：

class Node:
    def __init__(self,val,next=None,random=None):
        self.val = val  
        self.next = next
        self.random = random 
        
def copyRandomList(head):
    if not head:
        return 
    
    p = head 
    
    while p:
        node = Node(p.val)
        node.next = p.next  
        p.next = node  
        
        p = node.next 
        
    p = head  
    
    while p:
        node = p.next  
        node.random = p.random.next if p.random else None  
        p = node.next  
        
    p,p1 = head,Node(-1)
    cur = p1 
    
    while p:
        cur.next = p.next  
        cur = cur.next  
        
        p.next = cur.next 
        p = p.next 
    return p1.next 

def copyRandomList2(head):
    if not head:
        return  
    
    visitedHash = {}
    
    
    



if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2 
    node2.next = node3 
    node3.next = node4
    node1.random = node3 
    node2.random = node4 
    
    node = copyRandomList(node1)
    while node:
        print(node.val)
        node = node.next 

    