# 面试题25：二叉树中和为某一值的路径
# 题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。二叉树结点的定义如下：



class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 

res = []
def pathSum(root,target):
    if not root or not target:
        return  
    
    
    cur = [(root,target,str(root.val))]
    res = []
    while cur:
        node,target,path = cur.pop()
        if not node.left and not node.right:
            if node.val == target:
                res.append(path)
                
        if node.left:
            cur.append((node.left,target-node.val,path+"->"+str(node.left.val)))
            
        
        if node.right:
            cur.append((node.right,target-node.val,path+"->"+str(node.right.val)))
    return res 


def pathSumRecur(root,target,path,res):
    if not root or root.val > target:
        return  
    if root:
        path += str(root.val)
        if root.val == target:
            if not root.left and not root.right:
                res.append(path)
        else:
            path += "->"
            pathSumRecur(root.left,target-root.val,path,res)
            pathSumRecur(root.right,target-root.val,path,res)
    return res 


if __name__ == "__main__":
                
    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(12)
    node4 = TreeNode(4)
    node5 = TreeNode(7)
    node1.left = node2 
    node1.right = node3 
    node2.left = node4 
    node2.right = node5 
    
    # print(pathSum(node1,22))
    # binaryTreePaths(node1)
    # print(binaryTreePaths(node1))
    print(pathSumRecur(node1,22,"",[]))
    

    
            
        