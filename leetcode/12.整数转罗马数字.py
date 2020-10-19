#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#
# https://leetcode-cn.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (64.23%)
# Likes:    406
# Dislikes: 0
# Total Accepted:    114.6K
# Total Submissions: 178.2K
# Testcase Example:  '3'
#
# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
# 
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
# 
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# 
# 
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 
# 
# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
# 
# 示例 1:
# 
# 输入: 3
# 输出: "III"
# 
# 示例 2:
# 
# 输入: 4
# 输出: "IV"
# 
# 示例 3:
# 
# 输入: 9
# 输出: "IX"
# 
# 示例 4:
# 
# 输入: 58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.
# 
# 
# 示例 5:
# 
# 输入: 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# 
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        dic = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        for roman,value in dic.items():
            if value == 0:
                break  
            count,num = divmod(num,value)
            ans.append(roman*count)
        return ''.join(ans)
# @lc code=end

## 思路：贪心算法，把所有数字硬编码，按从大到小排列，相当于把原数字分解成罗马数字，一开始要选择尽可能大
## 的罗马数字，这样最后得到的结果长度才是最短的。3240为例，divmod(3240,1000) = (3,240), ans = ["M"*3],
## 下一轮循环，divmod(240,900) = (0,240), ans = ["MMM"].append(0*"D").

## 错误思路:一开始我直观认为要把数字拆解，3240 = 3 * 10 ** 3 + 2 * 10 **2 + 4 * 10**1 + 0*10**0，
## 这种思路未尝不可，只是很蠢，因为一开始没想到dic按从大到小排列寻找最接近的数。

## 做题教训:暴力解法固然可用，可是要明白算法不会仅仅考察暴力解法的