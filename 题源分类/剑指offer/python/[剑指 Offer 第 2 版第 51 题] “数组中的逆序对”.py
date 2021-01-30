# [剑指 Offer 第 2 版第 51 题] “数组中的逆序对”做题记录
# 第 51 题：数组中的逆序对
# 传送门：数组中的逆序对，牛客网 online judge 地址。

# 在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。

# 输入一个数组，求出这个数组中的逆序对的总数。

# 样例：

# 输入：[1,2,3,4,5,6,0]

# 输出：6

def mergeCount(nums,l,mid,r,temp):
    
    for i in range(l,r+1):
        temp[i] = nums[i]
        
    i,j,res = l,mid+1,0 
    
    for k in range(l,r+1):
        if i > mid:
            nums[k] = temp[j]
            j += 1 
        
        elif j > r:
            nums[k] = temp[i]
            i += 1 
            
        elif temp[i] <= temp[j]:
            nums[k] = temp[i]
            i += 1 
        else:
            nums[k] = temp[j]
            j += 1 
            res += (mid-i+1)
    return res  

def countInversionPairs(nums,l,r,temp):
    if l == r:
        return 0 
    
    mid = l + (r-l)//2 
    left_pairs = countInversionPairs(nums,l,mid,temp)
    right_pairs = countInversionPairs(nums,mid+1,r,temp)
    
    merge_pairs = 0 
    
    if nums[mid] > nums[mid+1]:
        merge_pairs = mergeCount(nums,l,mid,r,temp)
    return left_pairs+right_pairs+merge_pairs

def inversePairs(nums):
    l = len(nums)
    if l < 2:
        return 0 
    temp = [0 for _ in range(l)]
    return countInversionPairs(nums,0,l-1,temp)

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,0]
    print(inversePairs(nums))