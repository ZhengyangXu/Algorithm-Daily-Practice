# 第 37 题：序列化二叉树
# 传送门：序列化二叉树，牛客网 online judge 地址。

# 请实现两个函数，分别用来序列化和反序列化二叉树。

# 您需要确保二叉树可以序列化为字符串，并且可以将此字符串反序列化为原始树结构。

# 样例：

# 你可以序列化如下的二叉树 8 / \ 12 2 / \ 6 4 为："[8, 12, 2, null, null, 6, 4, null, null, null, null]"

# 注意:

class TreeNode:
    def __init__(self,val):
        self.val = val  
        self.left = None
        self.right = None  

class Solution:
    def serialize(self,root):
        res = ''
        if not root:
            return ''
        res += str(root.val)
        res += ' '
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res 
    
    def ser_iter(self,root):
        if not root:
            return 'Null'
        node = root  
        stack = []
        res = ''
        while node or stack:
            if node:
                stack.append(node) 
                res += ''+str(node.val)
                node = node.left  
            else:
                node = stack.pop()
                res += ' Null '
                node = node.right
        return res
    
    def deserialize(self,data):
        
        arr = data.split(' ')
        return self.__helper(arr)
    
    
    
    def __helper(self,arr):
        if arr:
            top = arr.pop(0)
            if top != '!':
                root = TreeNode(int(top))
                root.left = self.__helper(arr)
                root.right = self.__helper(arr)
                return root  
            else:
                return None 
            
            
if __name__ == "__main__":
    node8 = TreeNode(8)
    node12 = TreeNode(12)
    node2 = TreeNode(2)
    node6 = TreeNode(6)
    node4 = TreeNode(4)
    
    node8.left = node12  
    node8.right = node2  
    
    node2.left = node6  
    node2.right = node4  
    
    solution1 = Solution()
    
    ser = solution1.serialize(node8)            
    print(ser)
    
    ser2 = solution1.ser_iter(node8)
    print(ser2)