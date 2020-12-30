# 面试题5：从尾到头打印链表

# 题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。

class node:
    def __init__(self,val):
        self.val = val 
        self.next = None 
        

def reverse(head):
    if not head:
        return  
    
    reverse(head.next)
    print(head.val)


if __name__ == "__main__":
    node1 = node(1)
    node2 = node(2)
    node3 = node(3)
    node1.next = node2
    node2.next = node3
    reverse(node1)
    print("+++++++++++++++")
    head1 = None 
    reverse(head1)
    print("+++++++++++++++++++")
    node4 = node(4)
    reverse(node4)


