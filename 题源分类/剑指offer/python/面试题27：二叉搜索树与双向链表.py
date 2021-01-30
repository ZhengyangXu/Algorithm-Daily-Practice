# 面试题27：二叉搜索树与双向链表
# 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。
# 比如输入图4.12中左边的二叉搜索树，则输出转换之后的排序双向链表。

class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 
        

# def convertNode(treeNode,listNode):
#     if not treeNode:
#         return  
#     cur = treeNode 
#     # print(cur.val)
    
#     if cur.left:
#         print("left")
#         convertNode(cur.left,listNode)
        
#     cur.left = listNode 
    
#     if listNode:
#         listNode.right = cur  
    
#     listNode = cur  
    

    
#     if cur.right:
#         print("right")
#         convertNode(cur.right,listNode)
        
    
    
        
        
# def convert(root):
#     lastNode = None  
#     convertNode(root,lastNode)
    
#     head = lastNode 
#     while head and head.left:
#         head = head.left 
        
#     return head 

##################################################

def dfs1(root):
    if not root.left or not root.right:
        return (root,root)
    
    if root.left and root.right:
        ll,lr = dfs1(root.left)
        rl,rr = dfs1(root.right)
        
        lr.right = root  
        root.left = lr 
        root.right = rl 
        rl.left = root  
        return (ll,rr)
    
    if root.left:
        ll,lr = dfs1(root.left)
        lr.right = root  
        root.left = lr  
        return (ll,root)
    
    if root.right:
        rl,rr = dfs1(root.right)
        root.right = rl  
        rl.left = root  
        return(root,rr)
    
def convertNode1(TreeNode):
    if TreeNode is None:
        return  
    head,_ = dfs1(TreeNode)
    
    return head

#######################################

def convertNode2(TreeNode,lastNode):
    
    if not TreeNode:
        return  
    
    cur = TreeNode  
    
    if cur.left:
        convertNode2(cur.left,lastNode)
        
    cur.left = lastNode  
    
    if lastNode:
        lastNode.right = cur  

    lastNode = cur   
    
    if cur.right:
        convertNode2(cur.right,lastNode)
    
        

def convert2(root):

    lastNode = None
    tail = convertNode2(root,lastNode)
    while tail and tail.left:
        tail = tail.left 
        
    
    return tail
##########################################

# lastNode = None  
# res = None  
# def dfs2(root):
#     global lastNode,res
#     if root is None:
#         return  
#     if root.left:
#         dfs2(root.left)
    
#     if lastNode is None:
#         lastNode = root
#         res = root
#     else:
#         lastNode.right = root  
#         root.left = lastNode 
#         lastNode = root 
#     if root.right:
#         dfs2(root.right)      

# def convert2(root):
#     dfs2(root)
#     return lastNode 
        
    
    
# class Solution(object):

#     def __init__(self):
#         self.linked_list_tail = None
#         self.res = None

#     def convert(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         self.__dfs(root)
#         return self.res

#     # 中序遍历
#     def __dfs(self, root):
#         if root is None:
#             return
#         self.__dfs(root.left)

#         if self.linked_list_tail is None:
#             self.linked_list_tail = root
#             self.res = root
#         else:
#             self.linked_list_tail.right = root
#             root.left = self.linked_list_tail
#             self.linked_list_tail = root
#         self.__dfs(root.right)    
#########################################

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
    
    # hx = convert(node10)
    last = None
    tail = convertNode2(node10,last)
    print(tail.val)
    # while head:
    #     print(head.val)
    #     head= head.right

# head = convert2(node10)
# print(head.val)
# # while head:
#     print(head.val)
#     head = head.right 
# solution1 = Solution()

# head2 = solution1.convert(node10)
# print(head2.val)