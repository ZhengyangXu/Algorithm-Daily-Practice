# 设计一个有getMin功能的栈
# 【题目】实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
# 【要求】1.pop、push、getMin操作的时间复杂度都是O（1）。
# 2.设计的栈类型可以使用现成的栈结构。


class GetMinStack:
    
    def __init__(self):
        self.stackData = []
        self.stackMin = []
        
    
    def push(self,newNum):
        if len(self.stackMin) == 0:
            self.stackMin.append(newNum)
        elif newNum < self.getmin():
            self.stackMin.append(newNum)
        self.stackData.append(newNum)
        
    def pop(self):
        if len(self.stackData) == 0:
            return 
        value = self.stackData.pop()
        if value == self.getmin():
            self.stackMin.pop()
        
        return value 
    
    def getmin(self):
        if len(self.stackMin) == 0:
            return None  
        return self.stackMin[-1]

class GetMinStack2:
    
    def __init__(self):
        self.stackData = []
        self.stackMin = []
        
    def push(self,newNum):
        if len(self.stackMin) == 0 or newNum <= self.getmin():
            self.stackMin.append(newNum)
        elif newNum > self.getmin():
            self.stackMin.append(self.getmin())
        self.stackData.append(newNum)
        
    def pop(self):
        if len(self.stackData) == 0:
            return 
        self.stackMin.pop() 
        return self.stackData.pop()
        
        
    def getmin(self):
        if len(self.stackMin) == 0:
            return  
        return self.stackMin[-1]

if __name__ == "__main__":
    stack = GetMinStack2()
    
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(2)
    print(stack.stackData)
    print(stack.stackMin)
    print(stack.getmin())
    print(stack.getmin())
    print(stack.pop())
    print(stack.getmin())
    