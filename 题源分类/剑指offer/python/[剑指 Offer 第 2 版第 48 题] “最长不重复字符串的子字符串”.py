# [剑指 Offer 第 2 版第 48 题] “最长不重复字符串的子字符串”做题记录
# 第 48 题：最长不重复字符串的子字符串
# 传送门：最长不含重复字符的子字符串。

# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

# 假设字符串中只包含从’a’到’z’的字符。

# 样例：

# 输入："abcabc"

# 输出：3
from collections import Counter
def maxSubStr(s):
    if not s:
        return 0
    r,l = 0,0
    res = 0 
    window = Counter()  
    while r < len(s):
        c1 = s[r] 
        window[c1] += 1 
        r += 1 
        while window[c1] > 1:
            c2 = s[l]
            window[c2] -= 1 
            l += 1 
        res = max(res,r-l)
    return res  

def dpMaxSubStr(s):
    if not s:
        return 0 
    dp = [1 for _ in range(len(s))]
    dic = dict()    
    dic[s[0]] = 0 
    
    for i in range(1,len(s)):
        if s[i] not in dic:
            dp[i] = dp[i-1] + 1  
        else:
            if i - dic[s[i]] > dp[i-1]:
                dp[i] = dp[i-1] + 1 
                
            else:
                dp[i] = i - dic[s[i]]
                
        dic[s[i]] = i 
    return max(dp)

def blockSubStr(s):
    if not s:
        return 0  
    dic = dict() 
    res,block = 1,0  
    for i in range(len(s)):
        if s[i] in dic and dic[s[i]] >= block:
            block += dic[s[i]] + 1  
            
        res = max(res,i-block+1)
        dic[s[i]] = i  
    return res  
            
            
     


if __name__ == "__main__":
    s = "abcabc"
    print(maxSubStr(s))    
    print(dpMaxSubStr(s))
    print(blockSubStr(s))