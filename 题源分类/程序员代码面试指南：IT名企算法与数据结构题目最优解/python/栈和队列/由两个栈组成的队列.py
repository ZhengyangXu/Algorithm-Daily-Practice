# 由两个栈组成的队列【题目】编写一个类，用两个栈实现队列，
# 支持队列的基本操作（add、poll、peek）。
# 【难度】尉 ★★☆☆

class TwoStacksQueue:
    def __init__(self):
        self.stackPush = []
        self.stackPop = []
        
    def pushToPop(self):
        if not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
            
    def add(self,num):
        self.stackPush.append(num)
    
    def poll(self):
        if not self.stackPop and not self.stackPush:
            return 
        self.pushToPop()
        return self.stackPop.pop()
    
    def peek(self):
        if not self.stackPop and not self.stackPush:
            return  
        return self.stackPop[0]
    
if __name__ == "__main__":
    
    queue = TwoStacksQueue( )
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    queue.add(5)
    queue.poll()
    queue.poll()
    queue.add(6)
    queue.add(7)
    queue.add(8)
    queue.add(9)
    queue.add(10)
    queue.poll()
    queue.peek()