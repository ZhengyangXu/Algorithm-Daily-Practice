def merge(left,right):
    result = []
    
    m = n = 0
    while m <len(left) and n < len(right):
        if left[m] < right[n]:
            result.append(left[m])
            m += 1 
        else:
            result.append(right[n])
            n += 1 
            
    result += left[m:]
    result += right[n:]
    
    return result 

def mergesort(nums):
    if len(nums) < 2:
        return nums 
    
    mid = len(nums)>>1 
    
    left = nums[:mid]
    right = nums[mid:]
    
    return merge(mergesort(left),mergesort(right))


def mergesort_iter(nums):
    step = 2 
    length = len(nums)
    
    while step < 2*length:
        for i in range(0,length,step):
            left = nums[i:i+step//2]
            right = nums[i+step//2:i+step]
            nums[i:i+step] = merge(left,right)
        step *= 2 
    return nums

if __name__ == "__main__":
    nums = [1,2,5,3,4,7,3,7,9]
    print(mergesort(nums))
    print(mergesort_iter(nums))