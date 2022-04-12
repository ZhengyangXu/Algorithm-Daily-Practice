def mergesort(nums): ## 递归
    if len(nums)<2:
        return nums  
    mid = len(nums)>>1
    
    left = nums[:mid]
    right = nums[mid:]
    
    return merge(mergesort(left),mergesort(right))

def merge(left,right):
    res = []
    
    m = n = 0 
    while m < len(left) and n < len(right):
        if left[m] < right[n]:
            res.append(left[m])
            m += 1 
        else:
            res.append(right[n])
            n += 1 
    
    res += left[m:]
    res += right[n:]
    
    return res 


def mergesort2(nums): ## 迭代
    step = 2 
    length = len(nums)
    
    while step < 2*length:
        for i in range(0,length,step):
            left=nums[i:i+step//2]
            right = nums[i+step//2:i+step]
            nums[i:i+step] = merge(left,right)
            
        step *= 2 
    return nums



if __name__ == "__main__":
    nums = [1,2,4,3,2,5]
    print(mergesort(nums))
    print(mergesort2(nums))
    