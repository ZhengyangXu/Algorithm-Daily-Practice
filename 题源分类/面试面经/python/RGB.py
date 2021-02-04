##把一个乱序RGB数组，按RGB顺序排序

def rgb(nums):
    if not nums:
        return  
    
    left,right = 0,0 
    for i in range(len(nums)):
        if nums[i] == "R":
            if i != right:
                nums[i],nums[right] = nums[right],nums[i]
            if right != left:
                nums[right],nums[left] = nums[left],nums[right]
                
            left += 1 
            right += 1
        elif nums[i] == "G":
            if i != right:
                nums[i],nums[right] = nums[right],nums[i]
            right += 1 
    return nums  

if __name__ == "__main__":
    nums = ["R","B",'G',"R","B","G","R","B","B","G"]
    
    print(rgb(nums))