# 第 45 题：把数组排成最小的数
# 传送门：把数组排成最小的数，牛客网 online judge 地址。

# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

# 例如输入数组 [3, 32, 321]，则打印出这 3 个数字能排成的最小数字 321323。

# 样例：

# 输入：[3, 32, 321]

# 输出：321323

# 注意：输出数字的格式为字符串。

from functools import cmp_to_key 
def minNum(nums):
    # def cmp(x,y):
    #     return x+y<y+x
    
    if not nums:
        return ''
    
    key_func = cmp_to_key(lambda a,b:int(a+b)-int(b+a))
    result = sorted(map(str,nums),key=key_func)
    
    return ''.join(result)
    
if __name__ == "__main__":
    num = [3, 32, 321]
    # print(minNum())
    # print(list(map(str,num)))
    print(sorted(map(str,num)))
    
    