# 面试题24：二叉搜索树的后序遍历序列
# 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 



def isBSTree(postorder):
    if not postorder:
        return False 
    if len(postorder) <= 2:
        return True 
    root = postorder[-1]
    
    split = 0 
    while postorder[split] < root:
        split += 1 
        
    for num in postorder[split:len(postorder)-1]:
        if num <= root:
            return False
    
    left = isBSTree(postorder[:split])
    right = isBSTree(postorder[split:len(postorder)-1])
    
    return left and right
             
            
    
if __name__ == "__main__":

     postorder = [4,5,2,6,7,3,1]
     print(isBSTree(postorder))   