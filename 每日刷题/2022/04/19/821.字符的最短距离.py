#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#
# https://leetcode-cn.com/problems/shortest-distance-to-a-character/description/
#
# algorithms
# Easy (69.30%)
# Likes:    279
# Dislikes: 0
# Total Accepted:    53.1K
# Total Submissions: 72.8K
# Testcase Example:  '"loveleetcode"\n"e"'
#
# 给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。
#
# 返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近
# 的字符 c 的 距离 。
#
# 两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。
#
#
#
# 示例 1：
#
#
# 输入：s = "loveleetcode", c = "e"
# 输出：[3,2,1,0,1,0,0,1,2,2,1,0]
# 解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
# 距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
# 距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
# 对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
# 距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。
#
#
# 示例 2：
#
#
# 输入：s = "aaab", c = "b"
# 输出：[3,2,1,0]
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# s[i] 和 c 均为小写英文字母
# 题目数据保证 c 在 s 中至少出现一次
#
#
#


# @lc code=start
# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         n = len(s)
#         ans = [0] * n

#         idx = -n
#         for i, ch in enumerate(s):
#             if ch == c:
#                 idx = i
#             ans[i] = i - idx

#         idx = 2 * n
#         for i in range(n - 1, -1, -1):
#             if s[i] == c:
#                 idx = i
#             ans[i] = min(ans[i], idx - i)
#         return ans


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        pos = []
        res = [-1] * len(s)

        for i,k in enumerate(s):
            if k == c:
                pos.append(i)
                res[i] == 0

        i,j = 0,0
        while  i < len(res) and j < len(pos):
            if res[i] == 0:
                i += 1
                continue
            else:
                if j < len(s) - 1:
                    if i < pos[j]:
                        res[i] = pos[j] - i
                    elif i > pos[j] and i < pos[j+1] :
                        if i > pos[j] and i < pos[j+1]:

# @lc code=end
