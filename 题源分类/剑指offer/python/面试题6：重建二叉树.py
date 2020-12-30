# 面试题6：重建二叉树

# 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}
# 和中序遍历序列{4,7,2,1,5,3,8,6}，
# 则重建出图2.6所示的二叉树并输出它的头结点。
# 二叉树结点的定义如下：

class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.right = None 
        self.left = None 
        
def buildTree(preorder,inorder):
    
    if not preorder or not inorder:
        return 
    
    root = TreeNode(preorder[0])
    
    index = 0
    for i in range(len(inorder)):
        if inorder[i] == root.val:
            index = i 
            break 
    
    root.left = buildTree(preorder[1:index+1],inorder[:index])
    root.right = buildTree(preorder[index+1:],inorder[index+1:])
    
    return root  

def buildTree_iter(preorder,inorder):

        

def preorder2(root):
    if not root:
        return  
    
    print(root.val)
    preorder2(root.left)
    preorder2(root.right)
    
def preorder_iter(root):
    if not root:
        return  
    
    stack = []
    node = root 
    res = []
    while node or stack:
        if node:
            res.append(node.val)
            stack.append(node)
            node = node.left 
        else:
            node = stack.pop()
            node = node.right 
    return res  
            
    
def inorder2(root):
    if not root:
        return 
    
    inorder2(root.left)
    print(root.val)
    inorder2(root.right)
def inorder_iter(root):
    if not root:
        return 
    
    stack = []
    res = []
    node = root  
    
    while node or stack:
        while node:
            stack.append(node)
            node = node.left 
        node = stack.pop()
        res.append(node.val)
        node = node.right 
    return res 
    
def postorder(root):
    if not root:
        return  
     
    stack1 = [root]
    stack2 = []
    

    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        
        stack2.append(node.val)
    
    return stack2[::-1]
    
        
        
    

if __name__ == "__main__":
    preorder = [1,2,4,7,3,5,6,8]
    inorder = [4,7,2,1,5,3,8,6]
    root = buildTree(preorder,inorder)
    
    print("************TEST CASE1********")
    print("************前序遍历*********")
    preorder2(root)
    print(preorder_iter(root))
    print("************中序遍历*********")
    inorder2(root)
    print(inorder_iter(root))
    print("************后序遍历*********")
    print(postorder(root))
    
    print("************TEST CASE2********")
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]   
    root2 = buildTree(preorder,inorder)
    print("************前序遍历*********")
    preorder2(root2)
    print(preorder_iter(root2))
    print("************中序遍历*********")
    inorder2(root2)
    print(inorder_iter(root2))
    print("************后序遍历*********")
    print(postorder(root2))
    
    print("************TEST CASE3********")
    preorder = [1,2,3,4,5]
    inorder = [5,4,3,2,1]   
    root3 = buildTree(preorder,inorder)
    print("************前序遍历*********")
    preorder2(root3)
    print(preorder_iter(root3))
    print("************中序遍历*********")
    inorder2(root3)
    print(inorder_iter(root3))
    print("************后序遍历*********")
    print(postorder(root3))

    
