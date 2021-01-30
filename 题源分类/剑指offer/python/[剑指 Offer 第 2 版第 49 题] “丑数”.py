# [剑指 Offer 第 2 版第 49 题] “丑数”做题记录
# 第 49 题：丑数
# 传送门：丑数，牛客网 online judge 地址。

# 把只包含因子 
# 2
# 、
# 3
#  和 
# 5
#  的数称作丑数（Ugly Number）。

# 例如 
# 6
# 、
# 8
#  都是丑数，但 
# 14
#  不是，因为它包含因子 
# 7
# 。

# 求按从小到大的顺序的第 
# N
#  个丑数。

# 样例：

# 输入：5

# 输出：5

# 注意：习惯上我们把 
# 1
#  当做是第一个丑数。

def uglyNum(n):
    if n < 7:
        return n  
    res = [1,2,3,4,5,6]
    t2,t3,t5 = 3,2,1  
    
    for i in range(6,n):
        res.append(min(res[t2]*2,min(res[t3]*3,res[t5]*5)))
        
        while res[t2] * 2 <= res[i]:
            t2 += 1 
        
        while res[t3] * 2 <= res[i]:
            t3 += 1 
        
        while res[t5] * 2 <= res[i]:
            t5 += 1 
    return res[-1]

if __name__ == "__main__":
    print(uglyNum(9))