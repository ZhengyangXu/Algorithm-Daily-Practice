# 单调栈结构
# 【题目】
# 给定一个不含有重复值的数组arr，
# 找到每一个i位置左边和右边离i位置最近且值比arr
# [i]小的位置。返回所有位置相应的信息。
# 【举例】[插图]返回如下二维数组作为结果：
# [插图]-1表示不存在。所以上面的结果表示在arr中，
# 0位置左边和右边离0位置最近且值比arr[0]小的位置是-1和2；
# 1位置左边和右边离1位置最近且值比arr[1]小的位置是0和2；
# 2位置左边和右边离2位置最近且值比arr[2]小的位置是-1和-1……
# 进阶问题：给定一个可能含有重复值的数组arr，
# 找到每一个i位置左边和右边离i位置最近且值比arr[i]小的位置。
# 返回所有位置相应的信息。【要求】如果arr长度为N，
# 实现原问题和进阶问题的解法，时间复杂度都达到O（N）。
# 【难度】尉 ★★☆☆

def getNearLessNoRepeat(arr):
    if not arr:
        return [-1,-1]
    stack = [] 
    pos = [[-1,-1] for _ in range(len(arr))]
    for i in range(len(arr)):
        while stack and arr[i] < arr[stack[-1]]:
            p = stack.pop()
            pos[p] = [stack[-1] if stack else -1,i] 
        stack.append(i)
    
    while stack: 
        p = stack.pop()
        pos[p][0] = stack[-1] if stack else -1
                
    return pos 

def getNearLessRepeat(arr):
    if not arr: 
        return [-1,-1] 
    n = len(arr)
    stack = []
    res = [[-1,-1] for _ in range(n)]
    for i in range(n):
      
        while stack and arr[stack[-1][-1]] > arr[i]: 
        

  
if __name__ == "__main__":
    arr = [3,4,1,5,6,2,7]
    arr2 = [3,1,3,4,3,5,3,2,2]
    print(getNearLessNoRepeat(arr))
            