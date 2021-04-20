# 打印两个有序链表的公共部分
# 【题目】给定两个有序链表的头指针hed1和hed2，打印两个链表的公共部分。
# 【难度】士 ★☆☆☆

class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None 
    
def printCommonPrt(h1,h2):
    if not h1 or not h2:
        return 
    while h1 and h2:
        if h1.val < h2.val:
            print("11111")
            h1 = h1.next 
        elif h1.val > h2.val:
            print("222222")
            h2 = h2.next 
        else:
            print("xxxxxxx")
            print(h1.val)
            h1 = h1.next 
            h2 = h2.next 

if __name__ == "__min__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node11 = Node(1)
    node12= Node(2)
    node13= Node(3)
    node14= Node(4)
    
    node1.next = node2
    node2.next = node4 
    
    node11.next = node12 
    node12.next = node14
    
    printCommonPrt(node1,node11)