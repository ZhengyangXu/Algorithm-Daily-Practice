# 面试题22：栈的压入、弹出序列

# 题目：输入两个整数序列，第一个序列表示栈的压入顺序，
# 请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如序列1、2、3、4、5 是某栈的压栈序列，序列4、5、3、2、1 
# 是该压栈序列对应的一个弹出序列，但 4、3、5、1、2 就不可能是该压栈序列的弹出序列。

def isPopOrder(inorder,poporder):
    if not inorder or not poporder or len(inorder) != len(poporder):
        return False 
    
    stack = []
    j = 0
    for i in range(len(inorder)):
        stack.append(inorder[i])
        while j < len(poporder):
            if stack[-1] == poporder[j]:
                stack.pop()
                j += 1 
            else:
                break 
    return j == len(poporder) 


if __name__ == "__main__":
    print(isPopOrder([1,2,3,4,5],[4,5,3,2,1]))
    print(isPopOrder([1,2,3,4,5],[4,3,5,1,2]))
    print(isPopOrder([],[]))
    print(isPopOrder([1],[5]))