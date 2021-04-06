# 生成窗口最大值数组
# 【题目】
# 有一个整型数组arr和一个大小为w的窗口从数组的最左边滑到最右边，
# 窗口每次向右边滑一个位置。例如，数组为[4，3，5，4，3，3，6，7]，
# 窗口大小为3时：[插图]如果数组长度为n，窗口大小为w，则一共产生n-w+1个窗口的最大值。
# 请实现一个函数。
# ● 输入：整型数组arr，窗口大小为w。
# ● 输出：一个长度为n-w+1的数组res，res[i]表示每一种窗口状态下的最大值。
# 以本题为例，结果应该返回{5，5，5，4，6，7}。【难度】尉 ★★☆☆

from collections import deque
def getMaxWindow(arr,k):
    if not arr or not k: 
        return  
    res = []
    stack = []
    for i in range(len(arr)):
        
        if stack and stack[0] <= i - k:
            stack.pop(0)
            
            
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
            
        stack.append(i)
        
        if i >= k-1:
            res.append(arr[stack[0]])
        
    return res 

if __name__ == "__main__":
    arr = [4,3,5,4,3,3,6,7]
    k = 4
    
    print(getMaxWindow(arr,k))
        
        
        
        