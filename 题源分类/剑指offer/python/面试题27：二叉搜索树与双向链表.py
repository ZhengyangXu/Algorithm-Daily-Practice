# 面试题27：二叉搜索树与双向链表
# 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。
# 比如输入图4.12中左边的二叉搜索树，则输出转换之后的排序双向链表。

class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 
        

def convertNode(treeNode,listNode):
    if not treeNode:
        return  
    cur = treeNode 
    # print(cur.val)
    
    if cur.left:
        print("left")
        convertNode(cur.left,listNode)
        
    cur.left = listNode 
    
    if listNode:
        listNode.right = cur  
    
    listNode = cur  
    

    
    if cur.right:
        print("right")
        convertNode(cur.right,listNode)
        
    
    
        
        
def convert(root):
    lastNode = None  
    convertNode(root,lastNode)
    
    head = lastNode 
    while head and head.left:
        head = head.left 
        
    return head 

if __name__ == "__main__":
    node10 = TreeNode(10)
    node6 = TreeNode(6)
    node4 = TreeNode(4)
    node8 = TreeNode(8)
    node14 = TreeNode(14)
    node12 = TreeNode(12)
    node16 = TreeNode(16)
    
    node10.left = node6 
    node10.right = node14 
    node6.left = node4
    node6.right = node8 
    node14.left = node12 
    node14.right = node16 
    
    hx = convert(node10)
    
    print(hx)
