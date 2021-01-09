# 面试题12：打印1到最大的n位数
# 题目：输入数字n，按顺序打印出从1最大的n位十进制数。
# 比如输入3，则打印出1、2、3一直到最大的3位数即999。

def printN(n): #简单解法
    if not n:
        return 
    number = 1 
    for i in range(n):
        number *= 10 
        
    for i in range(number):
        print(i)
        
def printRecur(number,length,index):
    if index == length - 1:
        
if __name__ == "__main__":
    printN(3)
        