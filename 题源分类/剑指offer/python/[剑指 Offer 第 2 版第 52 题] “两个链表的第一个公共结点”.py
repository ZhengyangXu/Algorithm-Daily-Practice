# [剑指 Offer 第 2 版第 52 题] “两个链表的第一个公共结点”做题记录
# 第 52 题：两个链表的第一个公共结点
# 传送门：两个链表的第一个公共结点，牛客网 online judge 地址。

# 输入两个链表，找出它们的第一个公共结点。

# 样例：

# 给出两个链表如下所示： A： a1 → a2 ↘ c1 → c2 → c3 ↗ B：b1 → b2 → b3 输出第一个公共节点 c1。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def findCommonNode(nodeA,nodeB):
    if not nodeA or not nodeB:
        return None 
    
    sizeA,sizeB = 0,0 
    p1,p2 = nodeA,nodeB 
    while p1:
        sizeA += 1 
        p1 = p1.next  
        
    while p2:
        sizeB += 1 
        p2 = p2.next 
    
    if sizeA >= sizeB:
        h1,h2 = nodeA,nodeB 
    else:
        h1,h2 = nodeB,nodeA  
        
    for _ in range(abs(sizeA-sizeB)):
        h1 = h1.next  
    
    while h1 and h2 and h1.val != h2.val:
        h1 = h1.next  
        h2 = h2.next  
    
    if not h1 and not h2:
        return None  
    else:
        return h1  
    

def findCommonNode1(p1,p2):
    if p1 or not p2:
        return None  
    stack1,stack2 = [],[]
    
    node1,node2 = p1,p2  
    
    while node1:
        stack1.append(node1)
        node1 = node1.next 
        
    
    while node2:
        stack2.append(node2)
        node2 = node2.next 
    
    res = None  
    while stack1 and stack2:
        node1 = stack1.pop()
        node2 = stack2.pop()  
        if node1.val == node2.val:
            res = node1 
            continue  
        if not stack1 or not stack2:
            return None  
    return res  
            
        


if __name__ == "__main__":
    na1 = ListNode(1)
    nb1= ListNode(2) 
    na2 = ListNode(3)
    na3 = ListNode(4) 
    na4 = ListNode(5)
    na1.next =na2 
    na2.next = na3 
    na3.next = na4 
    nb1.next = na3 
    # node= findCommonNode(na1,nb1)
    # print(node.val)
    node2 = findCommonNode1(na1,nb1)
    print(node2.val)
        