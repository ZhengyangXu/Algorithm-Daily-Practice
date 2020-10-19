#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (29.65%)
# Likes:    1374
# Dislikes: 0
# Total Accepted:    98K
# Total Submissions: 328.9K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# 
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
# 
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3:
# 
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 示例 4:
# 
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 
# 
# 示例 5:
# 
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        # dp[i][j] 表示 s[:i] 与 p[:j] 是否匹配，各自前 i、j 个是否匹配
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True

        # s 为空串
        for j in range(1, p_len + 1):
            # 若 p 的第 j 个字符 p[j - 1] 是 '*'
            # 说明第 j - 1、j 位可有可无
            # 那么如果前 j - 2 个已经匹配上，前 j 个也可以匹配上
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j - 1] in {s[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] in {s[i - 1], '.'}:
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp[s_len][p_len]
# @lc code=end
#    def isMatch(self, s: str, p: str) -> bool:
#         memo = dict()
#         def dp(i,j):
#             if (i,j) in memo:
#                 return memo[(i,j)]
#             if j == len(p):
#                 return i == len(s)
            
#             first = i < len(s) and p[j] in {s[i],"."}
            
#             if j <= len(p) - 2 and p[j+1] == "*":
#                 ans = dp(i,j+2) or (first and dp(i+1,j))
#             else:
#                 ans = first and dp(i+1,j+1) 
#             memo[(i,j)] = ans   
#             return ans  
#         return dp(0,0)
