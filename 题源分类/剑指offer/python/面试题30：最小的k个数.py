# 面试题30：最小的k个数

# 题目：输入n个整数，找出其中最小的k个数。
# 例如输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

def partition(input,left,right):
    if left == right:
        return left 
    pivot = input[left]
    j = left 
    for i in range(left+1,right+1):
        if input[i] < pivot:
            j += 1 
            input[i],input[j] = input[j],input[i]
    input[left],input[j] = input[j],input[left]
    return j 

def getLeastNumbers(input,k):
    size = len(input)
    
    if size == 0:
        return []
    if k == size:
        return sorted(input)
    l,r = 0,size-1 
    while l <= r:
        p = partition(input,l,r)
        if p == k-1:
            return sorted(input[:p+1])
        elif p > k-1:
            r = p-1 
        else:
            l = p + 1 
            
################# 最大堆###########################
def getLeastNumbers2(input,k):
    size = len(input)
    if size == 0:
        return []
    if k == size:
        return input
    import heapq 
    l = []
    for num in input[:k]:
        heapq.heappush(l,-num)
    for num in input[k:]:
        top = l[0]
        if top < -num:
            heapq.heappushpop(l,-num)
    return [-num for num in l]
            
if __name__ == "__main__":
    
    nums = [1,5,4,2,4,2,4,6,3]
    # print(getLeastNumbers(nums,5))
    print(getLeastNumbers2(nums,5))