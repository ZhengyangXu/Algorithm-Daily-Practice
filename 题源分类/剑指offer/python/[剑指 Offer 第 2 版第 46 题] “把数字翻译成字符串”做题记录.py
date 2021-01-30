# 第 46 题：把数字翻译成字符串
# 传送门：把数字翻译成字符串。

# 给定一个数字，我们按照如下规则把它翻译为字符串：

# 0 翻译成 “a”，1 翻译成 “b”，……，11 翻译成“l”，……，25 翻译成 “z”。

# 一个数字可能有多个翻译。例如 12258 有 5 种不同的翻译，它们分别是 “bccfi”、“bwfi”、“bczi”、“mcfi” 和 “mzi”。

# 请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。

# 样例：

# 输入："12258"

# 输出：5


def getCount(s):
    if not s:
        return 0 
    s = str(s)
    l = len(s)
    
    dp = [1 for _ in range(l)]
    
    for i in range(1,l):
        cur = dp[i-1]
        
        num = int(s[i-1:i+1])
        
        if num > 9 and num < 26:
            if i - 2 < 0:
                cur += 1 
            else:
                cur += dp[i-2]
        dp[i] = cur  
    return dp[l-1]
    
if __name__ == "__main__":
    s = "12258" 
    print(getCount(s))