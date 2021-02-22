# 1. n个人围成一圈，编号是0~(n-1)，从第1个人（编号为0的人）从1开始报数，报到m的人出圈，
# 然后下面未出圈的人接着从1开始报数，直到所有人都出圈。请按出圈顺序输出出圈的人的编号。

class Node:
    def __init__(self,val):
        self.val = val  
        self.next = None  
        

def circleOut(n,m): ### 链表
    ## 创建环形链表
    head = Node(0)
    cur = head  
    
    for i in range(1,n):
        nex = Node(i)
        cur.next = nex  
        cur = nex 
    cur.next = head  
    
    count = 0  
    res = []
    pre,cur = None,head
    
    while head.next != head:
        if count == m:
            count = 0 
            res.append(cur.val)
            pre.next = cur.next  
            cur = pre.next 
            
        else:
            count += 1 
            pre = cur 
            cur = cur.next    
    return res
res = []
def circleOutRec(n,m):
    if n == 0:
        return n
    
    return (circleOutRec(n-1,m)+m)%n
    
    
    
if __name__ == "__main__":
    # print(circleOut(6,2))
    circleOutRec(6,2)
    print(res)