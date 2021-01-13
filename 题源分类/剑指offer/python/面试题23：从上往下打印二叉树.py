# 面试题23：从上往下打印二叉树

# 题目：从上往下打印出二叉树的每个结点，
# 同一层的结点按照从左到右的顺序打印。
# 例如输入图4.5中的二叉树，则依次打印出8、6、10、5、7、9、11。

class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 

def levelOrder(root):
    if not root:
        return 
    
    cur = [root]
    res = []
    while cur: 
        next = []
        for node in cur:
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
            res.append(node.val)
        cur = next 
    return res  


if __name__ == "__main__":
    
    
     node1 = TreeNode(1)
     node2 = TreeNode(2)
     node3 = TreeNode(3)
     node4 = TreeNode(4)
     node5 = TreeNode(5)
     node6 = TreeNode(6)
     node1.left = node2 
     node1.right = node3 
     node2.left = node4 
     node2.right = node5 
     node3.left = node6  
     
     print(levelOrder(node1))