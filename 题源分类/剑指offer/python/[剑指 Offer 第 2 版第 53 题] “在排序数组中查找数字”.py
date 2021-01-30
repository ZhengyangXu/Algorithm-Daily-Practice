# [剑指 Offer 第 2 版第 53 题] “在排序数组中查找数字”做题记录
# 第 53 题：数字在排序数组中出现的次数 （二分法典型问题）
# 传送门：数字在排序数组中出现的次数。

# 统计一个数字在排序数组中出现的次数。

# 例如输入排序数组 [1, 2, 3, 3, 3, 3, 4, 5] 和数字 3 ，由于 3 在这个数组中出现了 4 次，因此输出4。

# 样例：

# 输入：[1, 2, 3, 3, 3, 3, 4, 5] , 3

# 输出：4

def getFirstK(data,length,k,start,end):
    if start > end:
        return -1  
    mid = start + (end-start)//2 
    num = data[mid]
    
    if num == k:
        if (mid > 0 and data[mid-1] != k) or mid == 0:
            return mid  
        else:
            end = mid - 1 
    elif num < k:
        start = mid + 1 
    else:
        end = mid - 1 
    return getFirstK(data,length,k,start,end) 

def getLastK(data,length,k,start,end):
    if start > end:
        return -1 
    mid = start + (end-start)//2 
    num = data[mid]
    
    if num == k:
        if (num < length - 1 and data[mid+1] != k) or mid == length - 1:
            return mid  
        else:
            start = mid + 1 
            
    elif num<k:
        start = mid + 1 
    else:
        end = mid - 1 
    
    return getLastK(data,length,k,start,end)

def getNumOfK(data,k):
    
    if not data or not k:
        return 0 
    res = 0 
    first = getFirstK(data,len(data),k,0,len(data)-1)
    last = getLastK(data,len(data),k,0,len(data)-1)
    if first > -1 and last > -1:
        res = last - first  + 1 
    return res  


#########################################################
def helper(nums,k):
    size = len(nums)
    if size == 0:
        return 0 
    l,r = 0,size - 1
    while l < r:
        mid = l + (r-l)//2 
        if nums[mid] >= k:
            r = mid  
        else:
            l = mid + 1 
    
    if nums[l] != k:
        if nums[size-1] < k:
            return size  
        if nums[0] > k:
            return 0 
    return l  
def getNumberOfK2(nums,k):
    size = len(nums)
    if size == 0:
        return 0 
    return helper(nums,k+1) - helper(nums,k)




######################################################################
if __name__ == "__main__":
    data  = [1,1,3,3,3,3,5,5]
    # print(getNumOfK(data,3))
    print(getNumberOfK2(data,3))