# 面试题29：数组中出现次数超过一半的数字

# 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
# 超过数组长度的一半，因此输出2。

def moreThanHalfNum(nums):
    if not nums:
        return 0 
    
    res = nums[0]
    times = 1 
    
    for num in nums[1:]:
        if times == 0:
            res = num  
            times = 1 
        elif res == num:
            times += 1 
        else:
            times -= 1
            
    times = 0 
    for num in nums:
        if num == res:
            times += 1
            
    return res if times > len(nums)//2 else 0 

def quickSort(nums):
    if len(nums)<2:
        return nums
    pivot = len(nums)//2
    
    left = [x for x in nums if x < nums[pivot]]
    middle = [x for x in nums if x == nums[pivot]]
    right = [x for x in nums if x > nums[pivot]]
    
    return quickSort(left) + middle + quickSort(right)





if __name__ == "__main__":
    nums = [1,2,3,2,2,2,5,4,2]
    print(moreThanHalfNum(nums))
    
    x = quickSort(nums)
    print(x)
    