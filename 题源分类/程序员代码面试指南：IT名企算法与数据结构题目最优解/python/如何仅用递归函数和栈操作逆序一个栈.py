# 如何仅用递归函数和栈操作逆序一个栈
# 【题目】一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1。
# 将这个栈转置后，从栈顶到栈底为 1、2、3、4、5，也就是实现栈中元素的逆序，
# 但是只能用递归函数来实现，不能用其他数据结构。
# 【难度】尉 ★★☆☆

def getAndRemoveLastElement(stack):
    result = stack.pop()
    
    if not stack:
        return result
    else:
        last = getAndRemoveLastElement(stack)
        stack.append(result)
        return last  
    
def reverse(stack):
    if not stack:
        return  
    i = getAndRemoveLastElement(stack)
    reverse(stack)
    stack.append(i)
    

if __name__ == "__main__":
    stack = [1,2,3,4,5]
    reverse(stack)
    print(stack)
    
    
    stack2 = [1,2,3]
    print(getAndRemoveLastElement(stack2))
    print(stack2)
    