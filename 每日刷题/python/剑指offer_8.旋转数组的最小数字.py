# 面试题8：旋转数组的最小数字

# 题目：把一个数组最开始的若干个元素搬到数组的末尾，
# 我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，
# 输出旋转数组的最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，
# 该数组的最小值为1。

def findMin(nums):
    if not nums:
        return 
    
    size = len(nums)
    left,right = 0,size-1 
    
    mid = left  
    
    while nums[left] >= nums[right]:
        if right - left == 1:
            return nums[right]
            break  
        
        mid = (left+right)>>1 
        
        if nums[mid] == nums[left] == nums[right]:
            minvalue = float('inf')
            for i in range(size):
                if nums[i] < minvalue:
                    minvalue = nums[i]
            return minvalue 
        
        if nums[mid] > nums[left]:
            left = mid  
            
        else:
            right = mid  
    
    return nums[mid]


if __name__ == "__main__":
    nums = [5,6,7,8,1,2,3]
    print(findMin(nums))
    nums2 = [1,1,1,1,1,0,1,1]
    print(findMin(nums2))