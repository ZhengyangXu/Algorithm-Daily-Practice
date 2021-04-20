# 最大值减去最小值小于或等于num的子数组数量【题目】给定数组arr和整数num，
# 共返回有多少个子数组满足如下情况：[插图]max（arr[i..j]）
# 表示子数组arr[i..j]中的最大值，min（arr[i..j]）表示子数组arr[i..j]中的最小值。
# 【要求】如果数组长度为N，请实现时间复杂度为O（N）的解法。

from collections import deque
def getNum(arr,num):
    if not arr or len(arr) == 0 or num < 0:
        return 0 
    qmin = deque()
    qmax = deque()
    i,j = 0,0 
    n = len(arr)
    while i < n :
        while j < n:
            if qmin or qmin[-1] != j:
                while qmin and arr[qmin[-1]] >= arr[j]:
                    qmin.pop()
                qmin.appendTail(j)
                while qmax and arr[qmax[-1]] <= arr[j]:
                    qmax.pop()
                qmax.appendTail(j)
            
            if arr[qmax[0] ] - arr[amin[0]] > num:
                break;
            j += 1 
        res += j - 1
        if qmin[0] == i:
            qmin.popleft()
            
        if qmax[0] == i:
            qmax.popleft()
        i += 1 
        return res
    

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    num = 4
    
    getNum(arr,4)
    
    