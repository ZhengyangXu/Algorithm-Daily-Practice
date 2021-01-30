# 第 44 题：数字序列中某一位的数字
# 传送门：数字序列中某一位的数字。

# 数字以 0123456789101112131415… 的格式序列化到一个字符序列中。

# 在这个序列中，第 5 位（从 0 开始计数）是 5 ，第 13 位是 1 ，第 19 位是 4 ，等等。

# 请写一个函数求任意位对应的数字。

# 样例：

# 输入：13

# 输出：1

def digitAtIndex(n):
    if n < 10:
        return n 
    
    base = 9
    digits = 1
    
    while n - base * digits > 0:
        n -= base * digits 
        base *= 10 
        digits += 1
        
    index = n % digits 
    
    if index == 0:
        num = 10 ** (digits-1) + n // digits - 1 
        
        return num % 10 
    else:
        
        num = 10 ** (digits-1) + n//digits  
        for i in range(index,digits):
            num //= 10 
        return num % 10 
        

if __name__ == "__main__":
    print(digitAtIndex(1001))