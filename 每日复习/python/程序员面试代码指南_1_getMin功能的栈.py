# 设计一个有getMin功能的栈
# 【题目】实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
# 【要求】1.pop、push、getMin操作的时间复杂度都是O（1）。
# 2.设计的栈类型可以使用现成的栈结构。

## 思路：用两个栈，一个stackData保存数据，一个stackMin更新每次栈里的最小值。两种方案，一是push进
## stackdata后，如果该值比stackmin栈顶的值小，同时push进stackmin，否则不操作。

class GetMinStack:
    def __init__(self):
        self.stackData = []
        self.stackMin = []
        
    def push(self,newNum):
        if len(self.stackMin) == 0:
            self.stackMin.append(newNum)
        elif newNum < self.getMin():
            self.stackMin.append(nuewNum)
        self.stackData.append(newNum)
        
    
    def pop(self):
        if len(self.stackData) == 0:
            return  
        
        value = self.stackData.pop() 
        if value == self.getMin():
            self.stackMin.pop() 
        return value  
    
    
    def getMin(self):
        if len(self.stackData) == 0:
            return  
        
        return self.stackMin[-1]