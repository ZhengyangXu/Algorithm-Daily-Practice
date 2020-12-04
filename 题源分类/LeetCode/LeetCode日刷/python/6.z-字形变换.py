#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
# https://leetcode-cn.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (48.49%)
# Likes:    804
# Dislikes: 0
# Total Accepted:    162.8K
# Total Submissions: 335.1K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# 
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 
# 
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 
# 请你实现这个将字符串进行指定行数变换的函数：
# 
# string convert(string s, int numRows);
# 
# 示例 1:
# 
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 
# 
# 示例 2:
# 
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# 
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
# 
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        size = len(s)
        rownums = min(numRows,size)
        if rownums == 1:
            return s   
        res = ''
        cycle = 2 * rownums - 2  
        for i in range(rownums):
            for j in range(0,size,cycle):
                if j + i < size:
                    res += s[j+i]
                if (i != 0 and i != rownums - 1 and j + cycle - i < size):
                    res += s[j+cycle-i]
        return res  
        
# @lc code=end

#  def convert(self, s: str, numRows: int) -> str: 
#         res = ''
#         size = len(s)
#         numRows = min(size,numRows)
#         rows = ['']*size
#         if size < 2:
#             return s
#         down = False    
#         cur_row = 0 
#         for i in range(size):
#             rows[cur_row] += s[i]
#             if cur_row == 0 or cur_row == numRows - 1:
#                 down = not down
#             cur_row += 1 if down else -1
#         res = ''.join(rows)
#         return res  
# 横排遍历，先建立rownums个空类别row，代表每一行的字符。用down和cur_row来代表每一个字符的状态，如果cur_row不是0或者rownums-1
#,证明可以字符还处于向下遍历状态，此时每一个row都插入字符，如果cur_row等于0或者numrows证明每一行的字符都添加了一遍，开始反向添加字符刚开始down初始化
#为false，此时cur_row =0,down变为true，继续向下遍历，到numrows，down变为false，cur_row变为fasle，开始向上遍历...,最后把rownums个
#字符合并起来

## 规律法：
## 当 cur_row = 0时，添加的字符索引是,k(2*numrows-2)+i
## 当 cur_row = numrows-1时，添加的字符索引是 k(2*numrows-2)+i
## 当 cur_row 在中间时，添加的字符索引是k(2*numrows-2)+/- i 