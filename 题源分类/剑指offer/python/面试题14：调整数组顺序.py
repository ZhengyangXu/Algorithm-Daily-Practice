# 面试题14：调整数组顺序
# 使奇数位于偶数前面题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

def reOrder(nums):
    if not nums:
        return 
    j = 0
    for i in range(len(nums)):
        if nums[i]%2 != 0: 
            nums[i],nums[j] = nums[j],nums[i]
            j += 1 
    return nums 

def judge(number):
    if number % 2 == 0:
        return True 

def reOrder2(nums):
    if not nums:
        return  
    left,right = 0,len(nums)-1
    
    while left < right:
        while not judge(nums[left]):
            left += 1 
        while judge(nums[right]):
            right -= 1 
        
        if left < right:
            nums[left],nums[right] = nums[right],nums[left]
    
    return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print(reOrder(nums))
    print(reOrder2(nums))