#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#
# https://leetcode-cn.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (54.07%)
# Likes:    188
# Dislikes: 0
# Total Accepted:    22.3K
# Total Submissions: 41.2K
# Testcase Example:  '1'
#
# 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
# 
# 不要使用系统的 Math.random() 方法。
# 
# 
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: 1
# 输出: [7]
# 
# 
# 示例 2:
# 
# 
# 输入: 2
# 输出: [8,4]
# 
# 
# 示例 3:
# 
# 
# 输入: 3
# 输出: [8,1,10]
# 
# 
# 
# 
# 提示:
# 
# 
# rand7 已定义。
# 传入参数: n 表示 rand10 的调用次数。
# 
# 
# 
# 
# 进阶:
# 
# 
# rand7()调用次数的 期望值 是多少 ?
# 你能否尽量少调用 rand7() ?
# 
# 
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7()-1)*7+rand7()
            if num <= 40:
                return num%10+1
       
        
# @lc code=end

