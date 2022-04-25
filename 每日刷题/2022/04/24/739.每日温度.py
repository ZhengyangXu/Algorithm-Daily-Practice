#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
# https://leetcode-cn.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (68.96%)
# Likes:    1120
# Dislikes: 0
# Total Accepted:    286.3K
# Total Submissions: 415.1K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指在第 i
# 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
#
#
# 示例 1:
#
#
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
#
#
# 示例 2:
#
#
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
#
#
# 示例 3:
#
#
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]
#
#
#
# 提示：
#
#
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
#
#
#


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        n = len(temperatures)

        res = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res


# @lc code=end
