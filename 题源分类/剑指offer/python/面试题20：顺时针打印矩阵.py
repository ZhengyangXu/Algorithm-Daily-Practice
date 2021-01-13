# 面试题20：顺时针打印矩阵
# 题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。例如：如果输入如下矩阵：

def printMatrix(matrix):
    if not matrix:
        return 
    
    bottom,top,left,right = 0,len(matrix),0,len(matrix[0])
    
    while bottom < top and left < right:
        for i in range(right):
            print(matrix[bottom][i],end=',')
        bottom += 1
        
        for i in range(bottom,top):
            print(matrix[i][right-1],end=',')
        right -= 1
        
        for i in range(right-1,left-1,-1):
            print(matrix[top-1][i],end=',')
        top -= 1 
        
        for i in range(top-1,bottom,-1):
            print(matrix[i][left],end=',')
        
        left += 1 
        
def printMatrix2(matrix):
    if not matrix:
        return 
    
    endX = len(c)
    
        
if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    printMatrix(matrix)