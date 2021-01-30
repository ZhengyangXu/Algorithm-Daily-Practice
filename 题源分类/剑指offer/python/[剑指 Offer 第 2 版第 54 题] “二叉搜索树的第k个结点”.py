# [剑指 Offer 第 2 版第 54 题] “二叉搜索树的第k个结点”做题记录
# 第 54 题：二叉搜索树的第 
# k
#  大结点
# 传送门：二叉搜索树的第 k 大结点，牛客网 online judge 地址。

# 给定一棵二叉搜索树，请找出其中的第 
# k
#  小的结点。

# 你可以假设树和 
# k
#  都存在，并且 1≤ k ≤ 树的总结点数。

# 样例：

# 输入：root = [2, 1, 3, null, null, null, null] ，k = 3

# 2 / \ 1 3

# 输出：3

# 思路：使用栈模拟 BST 的中序遍历。
class TreeNode:
    def __init__(self,val):
        self.val = val  
        self.left = None  
        self.right = None 

def kthNode(root,k):
    if not root:
        return root  
    node = root 
    order = 0 
    stack = []
    res = []
    while stack or node:
        if node: 
            stack.append(node)
            node = node.left  
        else:
             node = stack.pop()
             order += 1 
             if order == k:
                 return node.val 
             node = node.right
             
            #  if len(res) == k:
            #      return res[-1].val  
##################################################
def kthNode2(root,k):
    if not root:
        return  
    
    stack = [(1,root)]
    while stack:
        type,node = stack.pop()
        if type == 0:
            k -= 1 
            if k == 0:
                return node.val
        else:
            if node.right:
                stack.append((1,node.right))
            stack.append((0,node))
            if node.left:
                stack.append((1,node.left))

        




#########################################################################             
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
    
    print(kthNode(node3,3))
    print(kthNode2(node3,3))