# 面试题21：包含min函数的栈

# 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。
# 在该栈中，调用min、push及pop的时间复杂度都是O（1）。


class getMinStack:
    def __init__(self):
        self.dataStack = []
        self.minStack = []
    
    def push(self,val):
        self.dataStack.append(val)
        if self.minStack:
            if self.minStack[-1] > val:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)
            
    def pop(self):
        if self.dataStack and self.minStack:
            self.minStack.pop()
            return self.dataStack.pop()
        return 
    
    def min(self):
        return self.minStack[-1]
    

if __name__ == "__main__":
    stack1 = getMinStack()
    stack1.push(2)
    stack1.push(4)
    stack1.push(3)
    stack1.push(1)
    print(stack1.min())
    stack1.push(6)
    stack1.pop()
    stack1.pop()
    print(stack1.min())