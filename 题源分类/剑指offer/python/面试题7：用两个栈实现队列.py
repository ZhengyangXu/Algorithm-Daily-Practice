# 面试题7：用两个栈实现队列题目：用两个栈实现一个队列。
# 队列的声明如下，请实现它的两个函数appendTail和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。

class queue:
    
    def __init__(self):
        self.stackAppend = []
        self.stackPop = []
        
    def appendToPop(self):
        if not self.stackPop:
            while self.stackAppend:
                self.stackPop.append(self.stackAppend.pop())
    
    
    def appendTail(self,val):
        self.stackAppend.append(val)
        
        
        
    
    def deleteHead(self):
        if not self.stackAppend and not self.stackPop:
            return   
        self.appendToPop()
        return self.stackPop.pop()
    

if __name__ == "__main__":
    
    queue1 = queue()
    queue1.appendTail(1)
    queue1.appendTail(2)
    queue1.appendTail(3)
    queue1.appendTail(4)
    queue1.appendTail(5)
    print(queue1.deleteHead())
    queue1.appendTail(6)
    queue1.appendTail(7)
    print(queue1.deleteHead())
    print(queue1.deleteHead())
        
        
    
    