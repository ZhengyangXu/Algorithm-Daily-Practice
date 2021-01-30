# 第 42 题：连续子数组的最大和
# 传送门：连续子数组的最大和，牛客网 online judge 地址。

# 输入一个 非空 整型数组，数组里的数可能为正，也可能为负。

# 数组中一个或连续的多个整数组成一个子数组。

# 求所有子数组的和的最大值。

# 要求时间复杂度为 
# O
# (
# n
# )
# 。

# 样例：

# 输入：[1, -2, 3, 10, -4, 7, 2, -5]

# 输出：18

def subMax(nums):
    if not nums:
        return 
    res = nums[0] 
    cur_sum = 0
    for i in range(len(nums)):
        if cur_sum > 0:
            cur_sum += nums[i]
        else:
            cur_sum = nums[i]
    
        res = max(res,cur_sum)    
    return res   

def subMaxDp(nums):
    if not nums:
        return  
    
    dp = nums[:]
    
    for i in range(1,len(nums)):
        dp[i] = max(dp[i-1]+nums[i],nums[i])
    
    return max(dp)

if __name__ == "__main__":
    print(subMax([1, -2, 3, 10, -4, 7, 2, -5]))
    print(subMaxDp([1, -2, 3, 10, -4, 7, 2, -5]))
        
        
        