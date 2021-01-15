# 面试题28：字符串的排列
# 题目：输入一个字符串，打印出该字符串中字符的所有排列。
# 例如输入字符串abc，则打印出由字符a、b、c所能排列出来的所有字符串
# abc、acb、bac、bca、cab和cba。

def backtrack(string,path):
    if len(path) == len(string):
        path = path[:]
        res.append(path)
        
    
    for letter in string:
        if letter in path:
            continue 
        path += letter 
        backtrack(string,path)
        path = path[:len(path)-1]


if __name__ == "__main__":
    res = []
    path = ""
    backtrack('abc',"")
    print(res)
