# [剑指 Offer 第 2 版第 56 题] “数字在排序数组中出现的次数”做题记录
# 第 56-1 题：数组中只出现一次的两个数字
# 传送门：数组中只出现一次的两个数字，牛客网 online judge 地址。

# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。

# 请写程序找出这两个只出现一次的数字。

# 你可以假设这两个数字一定存在。

def findNum(nums):
    if len(nums) < 2:
        return 
    
    xor = 0 
    for num in nums:
        xor ^= num 
        
    counter = 0 
    while xor & 1 == 0:
        xor >>= 1 
        counter += 1 
    
    res = [0,0]
    for num in nums:
        if (num >> counter) & 1 == 1:
            res[1] ^= num 
        else:
            res[0] ^= num  
    return res 


if __name__ == "__main__":
    nums = [1,2,2,3,3,4,6,]
    
    print(findNum(nums))
    




