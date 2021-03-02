# 给定一个double类型的数组arr，其中元素可正可负，返回子数组累乘的最大乘积；

# 如：

# arr  = [-2.5，4，0，3，0.5，8，-1]

# 则子数组[3，0.5，8]累乘获得最大乘积，返回12；


def maxProduct(nums):
    if not nums:
        return 
    
    ans = nums[0]
    
    for i in range(1,len(nums)):
        ans = max(ans*nums[i],-ans*nums[i],nums[i])
    
    return ans  

if __name__ == "__main__":
    print(maxProduct([-2.5,4,0,3,0.5,8,-1]))
    
    arr2 = [1,2,3,4,4,5,6]
    print(maxProduct(arr2))
