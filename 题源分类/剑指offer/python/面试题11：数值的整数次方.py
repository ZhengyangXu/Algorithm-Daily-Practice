# 面试题11：数值的整数次方


# 题目：实现函数 double Power（double base, int exponent），求 base的exponent次方。
# 不得使用库函数，同时不需要考虑大数问题。

def PowerWithUnsignedExponent(base,exp):
    if exp == 0:
        return 1 
    if exp == 1:
        return base 
    
    result = PowerWithUnsignedExponent(base,exp>>1)
    
    result *= result  
    
    if exp & 0x1 == 1:
        result *= base  
    
    return result 


if __name__ == "__main__":
    print(PowerWithUnsignedExponent(2,6))