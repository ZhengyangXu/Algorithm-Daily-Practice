# 面试题18：树的子结构
# 题目：输入两棵二叉树A和B，判断B是不是A的子结构。二叉树结点的定义如下：

class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 

def isSubTree(root1,root2): ## 递归
    
    if not root1 and not root2:
        return True 
    
    if not root1:
        print("false0")
        return False 
    
    
    if root1.val == root2.val:
        if (root1.left and not root2.left) or (not root1.left and root2.left):
            print("fasel1")
            return False 
        if (root1.right and not root2.right) or (not root1.right and root2.right):
            print("false2")
            return False 
        if not root1.left and not root2.left and not root1.right and not root2.right:
            return True


        if root1.left.val == root2.left.val and root1.right.val == root2.right.val:
            print("未进入递归")
            return True  
        else:
            print("进入递归")
            return isSubTree(root1.left,root2) or isSubTree(root1.right,root2)  
    else:
        print("进入递归")
        return isSubTree(root1.left,root2) or isSubTree(root1.right,root2)
    
    
def hasSubTree(roota,rootb):
    
    result = False  
    if roota and rootb:
        if roota.val == rootb.val:
            result = tree1HaveTree2(roota,rootb)
        if not result:
            result = hasSubTree(roota.left,rootb)
        if not result:
            result = hasSubTree(roota.right,rootb)
    return result 

def tree1HaveTree2(root1,root2):
    if not root2:
        return True 
    if not root1:
        return False 
    if root1.val != root2.val:
        return False 
    return tree1HaveTree2(root1.left,root2.left) and tree1HaveTree2(root1.right,root2.right)
    
    
    
    
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    
    nodea0 = TreeNode(8)
    nodea1 = TreeNode(8)
    nodea2 = TreeNode(7)
    nodea3 = TreeNode(9)
    nodea4 = TreeNode(2)
    nodea5 = TreeNode(4)
    nodea6 = TreeNode(7)
    
    nodeb1 = TreeNode(8)
    nodeb2 = TreeNode(9)
    nodeb3 = TreeNode(2)

    
    nodea0.left = nodea1 
    nodea0.right = nodea2
    nodea1.left = nodea3 
    nodea1.right = nodea4  
    nodea4.left = nodea5
    nodea4.right = nodea6
    
    nodeb1.left = nodeb2 
    # nodeb1.right = nodeb3 
    
    # print(isSubTree(nodea0,nodeb1))
    
    print(hasSubTree(nodea0,nodeb1))
    


    
    