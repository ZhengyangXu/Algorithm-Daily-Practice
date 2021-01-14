# 面试题26：复杂链表的复制
# 题目：请实现函数ComplexListNode*Clone（ComplexListNode*pHead），
# 复制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个结点外，
# 还有一个m_pSibling 指向链表中的任意结点或者NULL。结点的C++定义如下：

class CloneNode:
    def __init__(self,val):
        self.val = val  
        self.next = None  
        self.random = None 
        

def CloneNodes(head):
    if not head:
        return  
    
    p = head  
    while p:
        clone = CloneNode(1)
        clone.value = p.value  
        clone.next = p.next 
        p1.next = clone  
        
        p = clone.next  
        
    p = head  
    
    while p:
        clone = p.next  
        clone.random = p.random if p.random else None   
        
        p = clone  
        
    p1,pclone = head,head.next 
    p2 = pclone 
    
    while p1:
        p1.next = p2.next  
        p2.next = p1.next
        p1 = p1.next 
    
    return pclone  

if __name__ == "__main__":
    node1 = CloneNode(1)
    node2 = CloneNode(2)
    node3 = CloneNode(3)
    node4 = CloneNode(4)
    node1.next = node2 
    node2.next = node3 
    node3.next = node4
    node1.random = node3 
    node2.random = node4 
    
    clonenode = CloneNode(node1)
    print(clonenode.random.val)
    