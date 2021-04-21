#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (25.30%)
# Likes:    604
# Dislikes: 0
# Total Accepted:    82.1K
# Total Submissions: 324.1K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"111" 可以将 "1" 中的每个 "1" 映射为
# "A" ，从而得到 "AAA" ，或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。注意，"06" 不能映射为 "F"
# ，因为 "6" 和 "06" 不同。
# 
# 给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。
# 
# 题目数据保证答案肯定是一个 32 位 的整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20"
# 。由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
# 
# 
# 示例 4：
# 
# 
# 输入：s = "1"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 只包含数字，并且可能包含前导零。
# 
# 
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0 
        d1,d2 = 0,1 
        n = len(s)
        for i in range(1,n+1):
            d3 = 0 
            if s[i] != '0':
                d3 += d2 
            if i > 1 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                d3 += d1  
            
            d1,d2 = d2,d3
        return d3 
                

                
        

# @lc code=end

    # def numDecodings(self, s: str) -> int:
    #     if not s:
    #         return 0 
    #     dp = [0 for _ in range(len(s))]
    #     dp[0] = 0 if s[0] == '0' else 1
        
    #     for i in range(1,len(s)):
    #         if s[i] != '0':
    #             dp[i] += dp[i-1]
            
    #         num = int(s[i-1:i+1])
            
    #         if num > 9 and num < 27:
    #             if i - 2 < 0:
    #                 dp[i] += 1 
    #             else:
    #                 dp[i] += dp[i-2]
                
    #     return dp[-1]


    # def numDecodings(self, s: str) -> int:
    #     if not s:
    #         return 0 
    #     n = len(s)
    #     dp = [1] + [0] * n 
        
    #     for i in range(1,n+1):
    #         if s[i-1] != '0':
    #             dp[i] += dp[i-1]
                
    #         if i > 1 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
    #             dp[i] += dp[i-2]
                
    #     return dp[n]
#思路:
# 使用动态规划,dp[i] 代表s[:i]的解码方法。编码只有两种,一种是一位数字,只要s[i-1]不
##是0,当前位置的编码方法dp[i]就可以加1;一种是两位数,只要s[i-2:i]小于等于26，且s[i-2]不等于0，因
# 为有规定06不能算是2位数编码,dp[i]就等于dp[i] + dp[i-2],因为dp[i-2]是s[:i-2]的编码数,
##由于现在的两位数可以编码,所以在dp[i-2]的基础上加上dp[i]