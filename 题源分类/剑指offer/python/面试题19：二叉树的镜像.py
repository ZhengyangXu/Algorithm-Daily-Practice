# 面试题19：二叉树的镜像
# 题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。

class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 
        
        
def mirrior(root):
    if not root or not (root.left and root.right):
        return root 
    
    left = mirrior(root.right)
    right = mirrior(root.left)
    
    root.left = left 
    root.right = right  
    
    return root 

def mirrior_iter(root):
    if not root or not (root.left and root.right):
        return root
    
    new_root = TreeNode(root.val)  
    que1 = [root]
    que2 = [new_root] 
    
    while que1 and que2:
        node = que1.pop(0)
        new_node = que2.pop(0)
        print(node.val,new_node.val)
        if node.right:
            que1.append(node.right)
            new_node.left = TreeNode(node.right.val) 
            que2.append(new_node.left)
        if node.left:
            que1.append(node.left)
            new_node.right = TreeNode(node.left.val)
            que2.append(new_node.right)
            
    return new_root
            
def mirrior_iter2(root):
    if not root or not (root.left and root.right):
        return root
    que = [root]
    
    while que:
        node = que.pop(0)
        node.left,node.right = node.right,node.left 
        if node.right:
            que.append(node.right)
        if node.left:
            que.append(node.left)
    return root 
        

def preorder(root):
    if not root:
        return 
    print(root.val)
    preorder(root.left)
    preorder(root.right)

if __name__ == "__main__":
    
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(9)
    node4 = TreeNode(4)
    
    node0.left = node1 
    node0.right = node2 
    node1.left = node3 
    node1.right = node4 
    
    # root = mirrior(node0)
    # # print(root.val)
    # preorder(root)
    
    
    root = mirrior_iter(node0)
    # print(root.val)
    # preorder(root)