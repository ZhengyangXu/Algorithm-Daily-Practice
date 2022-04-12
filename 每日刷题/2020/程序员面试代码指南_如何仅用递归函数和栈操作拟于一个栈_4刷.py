# 如何仅用递归函数和栈操作逆序一个栈
# 【题目】一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1。
# 将这个栈转置后，从栈顶到栈底为 1、2、3、4、5，也就是实现栈中元素的逆序，
# 但是只能用递归函数来实现，不能用其他数据结构。
# 【难度】尉 ★★☆☆

def getAndReomveLast(nums):
    result = nums.pop()
    
    if not nums:
        return result  
    else:
        last = getAndReomveLast(nums)
        nums.append(result)
        return last 
    

def reverse(nums):
    if not nums:
        return 
    
    last = getAndReomveLast(nums)
    reverse(nums)
    nums.append(last)
    

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    reverse(nums)
    print(nums)
    