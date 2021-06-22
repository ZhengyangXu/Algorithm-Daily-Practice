# 剑指 Offer 38. 字符串的排列
# 输入一个字符串，打印出该字符串中字符的所有排列。

 

# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

# 示例:

# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
 

# 限制：

# 1 <= s 的长度 <= 8

# 通过次数119,873提交次数208,267


def permutation2(s) :
    if not s:
        return s 
    n = len(s)
    res = []
    path = ''
    visited = [0]*n 
    s = sorted(s)
    def backtrack(s,path):
        if len(path)== len(s):
            path = path[:]
            res.append(path)
        
        for i in range(n):
            if visited[i] or (i > 0 and not visited[i-1] and s[i] == s[i-1]):
                continue 
            path += s[i]
            visited[i] = True 
            backtrack(s,path)
            path = path[:-1]
            visited[i] = False 
    

    
    backtrack(s,path)

    return res 

def permutation(s):
    res = []
    c =  list(s)
    def dfs(j):
        if j == len(s) - 1:
            res.append("".join(c))
            return 
        dic = set() 
        for i in range(j,len(c)):
            if c[i] in dic:
                continue 
            dic.add(c[i])
            c[i],c[j] = c[j],c[i]
            dfs(j+1)
            c[i],c[j] = c[j],c[i]
    dfs(0)
    return res 
    

if __name__ == "__main__":
    s = "aba"
    print(permutation(s))