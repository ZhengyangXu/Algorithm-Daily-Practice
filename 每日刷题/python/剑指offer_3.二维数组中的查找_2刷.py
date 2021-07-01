# 面试题3：二维数组中的查找
# 题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

def findNum(matrix,num):
    if not matrix:
        return False  
    
    row,col = 0,len(matrix[0])-1
    
    while row < len(matrix) and col >= 0:
        if num == matrix[row][col]:
            print("有要找的数:{}".format(num)) 
            return True 
        elif num < matrix[row][col]:
            col -= 1 
            
        else:
            row += 1 
    print("没有要找的数:{}".format(num))       
    return False


if __name__=="__main__":
    matrix = [[1,2,3],[4,6,9],[10,11,12]]
    findNum(matrix,5)
    findNum(matrix,10)