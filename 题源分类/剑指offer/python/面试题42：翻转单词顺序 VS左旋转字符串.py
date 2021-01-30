# 面试题42：翻转单词顺序 VS左旋转字符串
# 题目一：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
# 例如输入字符串"I am astudent."，则输出"student.a am I"。

# 题目二：字符串的左旋转操作是把字符串前面
# 的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
# 比如输入字符串"abcdefg"和数字2，该函数将返回左旋转2位得到的结果"cdefgab"。


def reverseS(s):
    if not s:
        return  
    words = s.split(' ')
    return ' '.join(words[::-1])

def reverse(s,start,end):
    if start >= end:
        return 
    while start < end:
        s[start],s[end] = s[end],s[start]
        start += 1
        end -=1 
        
       

        

def reverseWords(s):
    if not s:
        return 
    
    size = len(s)
    arr = list(s)
    
    reverse(arr,0,size-1)
    begin,index = 0,0 
    
    while index < size:
        if arr[index] == ' ':
            reverse(arr,begin,index-1)
            begin = index + 1 
        index += 1 
    reverse(arr,begin,size-1)
    
    return ''.join(arr)

def leftRotate(s,n):
    if not s or n % len(s) == 0:
        return s 
    n = n%len(s)
    arr = list(s)
    reverse(arr,0,len(s)-1)
    reverse(arr,0,len(s)-1-n)
    reverse(arr,len(s)-n,len(s)-1)
    
    return ''.join(arr)

if __name__ == "__main__":
    s = "I am a student."
    print(reverseWords(s))
    
    s2 = "abcdefg"
    print(leftRotate(s2,2))