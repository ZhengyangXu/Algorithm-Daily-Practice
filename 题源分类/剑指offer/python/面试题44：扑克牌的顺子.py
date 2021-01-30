# 面试题44：扑克牌的顺子
# 题目：从扑克牌中随机抽 5张牌，
# 判断是不是一个顺子，即这 5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，
# 而大、小王可以看成任意数字。

def isCoutinuous(numbers):
    if len(numbers) < 5:
        return False  
    
    maxnum = -1
    minnum = 14 
    
    flag = 0 
    
    for number in numbers:
        if number < 0 or number > 13:
            return False  
        if number == 0:
            continue 
        
        if (flag >> number) & 1 == 1:
            return False  
        
        flag |= 1 << number  
        
        if number < minnum:
            minnum = number  
        
        if number > maxnum:
            maxnum = number  
        
        if maxnum - minnum >= 5:
            return False  
    return True 
        
def isCoutinuous2(numbers):
    length = len(numbers)
    if not numbers or length < 1:
        return False  
    
    sortnums = sorted(numbers)
    
    numberOfZero = 0
    numberOfGap = 0 
    
    for i in range(length):
        if numbers[i] == 0:
            numberOfZero += 1 
    small = numberOfZero 
    big = small + 1 
    while big < length:
        if numbers[small] == numbers[big]:
            return False  
        
        numberOfGap += numbers[big] - numbers[small] - 1 
        small = big  
        big += 1       
        
    return numberOfGap > numberOfZero 
    
if __name__ == "__main__":
    print(isCoutinuous([1,2,0,4,0]))
    
    
    print(isCoutinuous2([1,2,3,4,6]))