# 面试题9：斐波那契数列题目一：写一个函数，输入n，
# 求斐波那契（Fibonacci）数列的第n项。斐波那契数列的定义如下：
import numpy as np
def fib(n):
    if n <= 2:
        return 1 
    
    return fib(n-1)+fib(n-2)

memo = {}
def fib_memo(n):
    if n <= 2:
        return 1 
    if n in memo:
        return memo[n]
    
    memo[n] = fib(n-1)+fib(n-2)
    
    return memo[n]


def fib_iter(n):
    
    a,b = 1,1 
    
    if n <= 2:
        return 1 
    
    for _ in range(n-2):
        a,b = b,a+b
    
    return b 


def matrixMulti(A,B):
    length = len(A)
    width = len(B[0])
    res = [[0]*width for _ in range(length)]
    print(res)
    for i in range(length):
        for j in range(width):
            for k in range(len(B)):
                # print("i:{},j:{},k:{}".format(i,j,k))
                # print("".format(i,k,A[i][k],k,j,B[k][j]))
                # print("res[{}][{}]:{}".format(i,j,res[i][j]))
                res[i][j] += A[i][k] * B[k][j]
                # print("A[{}][{}]:{}*B[{}][{}]:{}=res[{}][{}]:{}".format(i,k,A[i][k],k,j,B[k][j],i,j,res[i][j]))
    return res 

def fibLog(matrix,n):
    
    res = [[1,0],[0,1]]
    
    tmp = matrix 
    
    while n > 0:
        
        if n & 1 != 0:
            res = np.dot(res,tmp)
        
        tmp = np.dot(tmp,tmp)
        
        n >>= 1 
    return res
    
    
    # if n == 0:
    #     return [[1,0],[0,1]]

    # if n == 1:
    #     return matrix
    
    # res = fibLog(matrix,n>>1)
    
    # res = np.dot(res,res)
    
    # if n & 0x1 == 1:
    #     res = np.dot(matrix,res)

    
    return res

    
    
            
               


if __name__ == "__main__":
    # print(fib(5))
    # print(fib(10))
    # print(fib_memo(10))
    # print(fib_iter(10))
    
    # A = [[1,2,3],[4,5,6]]
    # B = [[1,2],[3,4],[5,6]]
    # print(matrixMulti(A,B))
    # print(matrixMulti([[1,1],[1,0]],[[1,1],[1,0]]))
    print(fibLog([[1,1],[1,0]],3))
    # print(np.dot([[1,1],[1,0]],[[1,1],[1,0]]))