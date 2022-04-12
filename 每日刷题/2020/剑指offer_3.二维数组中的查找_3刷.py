# 面试题3：二维数组中的查找
# 题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


def findNum(matrix,num):
    
    row,col = 0,len(matrix[0])-1
    
    while row < len(matrix) and col >= 0:
        if num == matrix[row][col]:
            return True  
        elif num > matrix[row][col]:
            row += 1 
        else:
            col -= 1 
            
    return False 

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(findNum(matrix,6))
    print(findNum(matrix,10))
            