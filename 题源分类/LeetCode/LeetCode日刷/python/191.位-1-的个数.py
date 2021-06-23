# '''Author: your name
# Date: 2021-03-22 17:04:25
# LastEditTime: 2021-03-22 17:11:44
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: \反射e:\代码练习\每日一刷\题源分类\LeetCode\LeetCode日刷\python\191.位-1-的个数.py
# '''
#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#
# https://leetcode-cn.com/problems/number-of-1-bits/description/
#
# algorithms
# Easy (73.35%)
# Likes:    307
# Dislikes: 0
# Total Accepted:    137.8K
# Total Submissions: 187.9K
# Testcase Example:  '00000000000000000000000000001011'
#
# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
#
#
#
# 提示：
#
#
# 请注意，在某些语言（如
# Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
# 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
#
#
#
#
# 示例 1：
#
#
# 输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
#
#
# 示例 2：
#
#
# 输入：00000000000000000000000010000000
# 输出：1
# 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
#
#
# 示例 3：
#
#
# 输入：11111111111111111111111111111101
# 输出：31
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
#
#
#
# 提示：
#
#
# 输入必须是长度为 32 的 二进制串 。
#
#
#
#
#
#
#
# 进阶：
#
#
# 如果多次调用这个函数，你将如何优化你的算法？
#
#
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = (n & 0x55555555) + ((n >> 1)  & 0x55555555);
        n = (n & 0x33333333) + ((n >> 2)  & 0x33333333);
        n = (n & 0x0f0f0f0f) + ((n>> 4)  & 0x0f0f0f0f);
        n = (n & 0x00ff00ff) + ((n >> 8)  & 0x00ff00ff);
        n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff);
        return n;



# @lc code=end
    def hammingWeight(self, n: int) -> int:

        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1

        return count

    def hammingWeight(self, n: int) -> int:

        count = 0
        while n:
            count += 1
            n &= n-1

        return count

    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            count += (n >> i) & 1

        return count
# 0xaaaaaaaa = 10101010101010101010101010101010 (偶数位为1，奇数位为0）

# 0x55555555 = 1010101010101010101010101010101 (偶数位为0，奇数位为1）

# 0x33333333 = 110011001100110011001100110011 (1和0每隔两位交替出现)

# 0xcccccccc = 11001100110011001100110011001100 (0和1每隔两位交替出现)

# 0x0f0f0f0f = 00001111000011110000111100001111 (1和0每隔四位交替出现)

# 0xf0f0f0f0 = 11110000111100001111000011110000 (0和1每隔四位交替出现)
