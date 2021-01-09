# 面试题10：二进制中1的个数题目：请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。

# 例如把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。

def oneNum(n): ##负数会死循环
    count = 0
    while n > 0:
        if n & 1 != 0:
            count += 1
        n >>= 1
    return count  

def oneNum2(n):
    flag = 1
    count = 0 
    for i in range(32):
        if flag & n:
            count += 1 
        flag <<= 1
    return count 

def numberOf1(n):
    if n < 0:
        n = n & 0xFFFFFFFF ### n & 0xFFFF FFFF 就能表示出任意一个数在计算机的表示方式！
    count = 0 
    while n:
        count += 1 
        n = (n-1) & n
    return count 
    
    

if __name__=="__main__":

    # print(oneNum(8))
    # print(oneNum2(9))
    # print(oneNum2(-100))
    print(numberOf1(-100))