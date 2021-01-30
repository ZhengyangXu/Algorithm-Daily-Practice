# [剑指 Offer 第 2 版第 55_2 题] “平衡二叉树”做题记录
# 第 55-2 题：平衡二叉树
# 传送门：平衡二叉树，牛客网 online judge 地址。

# 输入一棵二叉树的根结点，判断该树是不是平衡二叉树。

# 如果某二叉树中任意结点的左右子树的深度相差不超过 $1$，那么它就是一棵平衡二叉树。

# 注意：

# 规定空树也是一棵平衡二叉树。
# 样例：

# 输入：二叉树 [5,7,11,null,null,12,9,null,null,null,null] 如下所示， 5 / \ 7 11 / \ 12 9 输出：true
class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.right = None 
        self.left = None 

def isBalanced(root):
    if not root:
        return True  
    
    def treeDepth(root):
        if not root:
            return 0 
        
        return max(treeDepth(root.left),treeDepth(root.rightl))+1 
    return abs(treeDepth(root.left)-treeDepth(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right)


def isBalanced2(root):
    if not root:
        return True 
    flag = True  
    def dfs(root):
        if not root:
            return 0  
        
        left = dfs(root.left)+1 
        right = dfs(root.right)+1 
        
        if abs(left-right) > 1:
            flag = False  
        return max(left,right)
    
if __name__ == "__main__":
     