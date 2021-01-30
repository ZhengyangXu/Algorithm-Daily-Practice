# [剑指 Offer 第 2 版第 55-1 题] “二叉树的深度”做题记录
# 第 55-1 题：二叉树的深度
# 传送门：二叉树的深度，牛客网 online judge 地址。。

# 输入一棵二叉树的根结点，求该树的深度。

# 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

# 样例：

# 输入：二叉树 [8, 12, 2, null, null, 6, 4, null, null, null, null] 如下图所示： 8 / \ 12 2 / \ 6 4 输出：3

class TreeNode:
    def __init__(self,val):
        self.val = val  
        self.left = None  
        self.right = None 

def treeDepth(root):
    if not root:
        return 0 

        
    return max(treeDepth(root.left),treeDepth(root.right)) + 1 

def treeDepthIter(root):
    if not root:
        return 0 
    cur = [(1,root)]
    max_depth = 0 
    while cur: 
        depth,node = cur.pop()
        if node.left:
            cur.append((1+depth,node.left))
        if node.right:
            cur.append((1+depth,node.right))
            
        max_depth = max(max_depth,depth)
    
    return max_depth 
            

if __name__ == "__main__":
    node3 = TreeNode(3)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    
    node3.left = node1 
    node3.right = node4 
    node1.right = node2
    node4.right = node5  
    
    
    print(treeDepth(node3))
    print(treeDepthIter(node3))
    