# LeetCode 156. 上下翻转二叉树

# 给定一个二叉树，其中所有的右节点要么是具有兄弟节点（拥有相同父节点的左节点）的叶节点，要么为空
# 将此二叉树上下翻转并将它变成一棵树， 原来的右节点将转换成左叶节点。返回新的根。

# 例子:

# 输入: [1,2,3,4,5]

#     1
#    / \
#   2   3
#  / \
# 4   5

# 输出: 返回二叉树的根 [4,5,2,#,#,3,1]

#    4
#   / \
#  5   2
#     / \
#    3   1  
# 说明:

# 对 [4,5,2,#,#,3,1] 感到困惑? 下面详细介绍请查看 二叉树是如何被序列化的。

# 二叉树的序列化遵循层次遍历规则，当没有节点存在时，'#' 表示路径终止符。

# 这里有一个例子:

#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# 上面的二叉树则被序列化为 [1,2,3,#,#,4,#,#,5].
class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 
        
def upsideDownBinaryTree(root):
    
    if not root or not root.left:
        return root 
    
    left = root.left  
    right = root.right 
    root.left = None 
    root.right = None 
    p = upsideDownBinaryTree(left)
    left.left = right 
    left.right = root  
    return p  
              
def upsideDownBinaryTree2(root):
    
    cur,pre,nex,tmp = root,None,None,None  
    while cur: 
        nex = cur.left  
        cur.left = tmp  
        tmp = cur.right  
        cur.right = pre 
        pre = cur  
        cur = nex  
    return pre           
if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2 
    node1.right = node3 
    node2.left = node4 
    node2.right = node5 
    
    # x = upsideDownBinaryTree(node1)
    # print(x.val)
    
    y = upsideDownBinaryTree2(node1)
    print(y.val)