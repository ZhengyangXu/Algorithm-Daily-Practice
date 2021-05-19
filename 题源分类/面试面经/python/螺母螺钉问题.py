# 题目：

# 给你一堆螺母和螺帽，每个螺母都有一个相对应的螺帽，
# 但是他们之间的对应关系已经打乱。
# 你可以比较螺母和螺帽的大小关系，
# 但是你无法比较螺母和螺母的大小关系，
# 你也无法比较螺帽和螺帽的大小关系。时间复杂度nlogn。

def fix(n,b,low,high):
    print("n:",n)
    print("b:",b)
    if low < high:
        tmp = n[low]
        i,j = low,high
        while i < j:
            while i < j and b[i] < tmp:
                i += 1
            while i < j and b[j] > tmp:
                j -= 1

            if i < j:
                b[i],b[j] = b[j],b[i]
        b[i] = tmp
        b[low],b[i] = b[i],b[low]

        tmp2 = b[low+1]
        i,j = low+1,high
        while i < j:
            while i < j and n[i] < tmp2:
                i += 1
            while i < j and n[j] > tmp2:
                j -= 1
            if i < j:
                n[i],n[j] = n[j],n[i]
            n[i] = tmp2
            n[low+1],n[i] = n[i],n[low+1]

            fix(n,b,low+2,i);
            fix(n,b,i+1,high)
        
            


if __name__ == "__main__":
    nuts = [5, 9, 3, 7, 1, 8, 2, 4, 6]
    bolts = [7, 4, 1, 2, 5, 6, 9, 8, 3]
    
    fix(nuts,bolts,0,len(nuts)-1)
    
    print
