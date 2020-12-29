def merge(left,right):
    
    result = []
    
    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
            
    while left:
        result.append(left.pop(0))
        
    while right:
        result.append(right.pop(0))
    return result 

def mergesort(nums):
    
    if len(nums) == 1:
        return nums
    
    mid = len(nums)//2  
    
    left = nums[:mid]
    right = nums[mid:]
    
    return merge(mergesort(left),mergesort(right))


########## 迭代归并

def mergesort_iter(nums):
    
    step = 2 
    size = len(nums)
    
    while step < 2*size:
        
        for i in range(0,size,step):
            left = nums[i:i+step//2]
            right = nums[i+step//2:i+step]
            print("left:{},right:{}".format(left,right))
            m,n = 0,0
            res = []
            while m<len(left) and n<len(right):
                if left[m] < right[n]:
                    res.append(left[m])
                    m += 1
                else:
                    res.append(right[n])
                    n += 1
            res += left[m:]
            res += right[n:]
            nums[i:i+step] = res
            print(res)
            print(nums)
            print(step)
        step *= 2   
    return nums 




# def merge_sort2(nums):
#     length = len(nums)
#     interval = 2
#     i = 0
#     while interval < length:
#         for i in range(0, length, interval):
#             nums[i:i+interval] = merge2(nums[i:i+interval//2], nums[i+interval//2:i+interval])
#         interval *= 2
#     return nums
       
# def merge2(left, right):
#     res = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     res += left[i:]
#     res += right[j:]
#     return res
        

if __name__ == "__main__":
    nums = [7,6,5,4,3,2,1]
    
    #print(mergesort(nums))
    
    
    print(mergesort_iter(nums))
    