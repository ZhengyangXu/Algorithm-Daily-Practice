#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#
# https://leetcode-cn.com/problems/di-string-match/description/
#
# algorithms
# Easy (73.41%)
# Likes:    336
# Dislikes: 0
# Total Accepted:    45.8K
# Total Submissions: 59.6K
# Testcase Example:  '"IDID"'
#
# 由范围 [0,n] 内所有整数组成的 n + 1 个整数的排列序列可以表示为长度为 n 的字符串 s ，其中:
#
#
# 如果 perm[i] < perm[i + 1] ，那么 s[i] == 'I'
# 如果 perm[i] > perm[i + 1] ，那么 s[i] == 'D'
#
#
# 给定一个字符串 s ，重构排列 perm 并返回它。如果有多个有效排列perm，则返回其中 任何一个 。
#
#
#
# 示例 1：
#
#
# 输入：s = "IDID"
# 输出：[0,4,1,3,2]
#
#
# 示例 2：
#
#
# 输入：s = "III"
# 输出：[0,1,2,3]
#
#
# 示例 3：
#
#
# 输入：s = "DDI"
# 输出：[3,2,0,1]
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^5
# s 只包含字符 "I" 或 "D"
#
#
#


# @lc code=start
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        lo, hi = 0, n
        perm = [0] * (n + 1)

        for i, ch in enumerate(s):
            if ch == 'I':
                perm[i] = lo
                lo += 1
            else:
                perm[i] = hi
                hi -= 1
            perm[n] = lo

        return perm


# @lc code=end
# def diStringMatch(self, s: str) -> List[int]:
#     n = len(s)
#     c, j = 0, n
#     res = []
#     for i in range(n):
#         if s[i] == "D":
#             res.append(j)
#             j -= 1
#         else:
#             res.append(c)
#             c += 1
#     res.append(j)
#     return res
