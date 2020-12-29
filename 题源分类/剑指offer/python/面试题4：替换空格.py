# 面试题4：替换空格
# 题目：请实现一个函数，把字符串中的每个空格替换成"%20"。
# 例如输入“We are happy.”，则输出“We%20are%20happy.”。


def replaceSpace(str):
    
    if not str:
        return ""
    
    count = 0
    for i in range(len(str)):
        if str[i] == " ":
            count += 1 
            
    ans = ['']*(len(str)+2*count)
    
    p1,p2 = len(str)-1,len(ans)-1
    
    while p1 >= 0 and p2 >= 0:
        if str[p1] == " ":

            for i in (["0","2","%"]):
                ans[p2] = i
                p2 -= 1
            p1 -= 1
        else:
            ans[p2] = str[p1]
            p2 -= 1 
            p1 -= 1 
            
    return "".join(ans)

if __name__=="__main__":
    str = "I have your mom"
    print(replaceSpace(str))
                
    