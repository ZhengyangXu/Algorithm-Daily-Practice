#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (44.13%)
# Likes:    1908
# Dislikes: 0
# Total Accepted:    244.6K
# Total Submissions: 554.3K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
# 示例 1:
#
#
#
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#
#
# 示例 2：
#
#
#
#
# 输入： heights = [2,4]
# 输出： 4
#
#
#
# 提示：
#
#
# 1
# 0
#
#
#


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ##2.单调栈 优化 线性时间
        n = len(heights)
        left, right = [0] * n, [0] * n

        mnstack = []
        for i in range(n):
            while mnstack and heights[i] <= heights[mnstack[-1]]:
                right[mnstack[-1]] = i
                mnstack.pop()

            left[i] = mnstack[-1] if mnstack else -1
            mnstack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i]
                  for i in range(n)) if n > 0 else 0

        return ans


# @lc code=end

# def largestRectangleArea(self, heights: List[int]) -> int:
#     ##1.暴力解法 以当前柱子高度为基准，向两边扩，找到高度比它低的

#     n = len(heights)
#     res= -float('inf')
#     for i in range(n):
#         left,right = i,i
#         curheights = heights[i]
#         while left > 0 and curheights <= heights[left-1]:
#             left -= 1

#         while right < n - 1 and curheights<=heights[right+1]:
#             right += 1

#         res = max(res, (right-left+1)*curheights)

#     return res
# def largestRectangleArea(self, heights: List[int]) -> int:
#     ##2.
#     n = len(heights)
#     res = 0

#     stack = []

#     for i in range(n):
#         while stack and heights[i] < heights[stack[-1]]:
#             curheight = heights[stack.pop()]

#             while stack and curheight == heights[stack[-1]]:
#                 stack.pop()

#             if stack:
#                 curwidth = i - stack[-1] - 1
#             else:
#                 curwidth = i

#             res = max(res, curheight * curwidth)
#         stack.append(i)

#     while stack:

#         curheight = heights[stack.pop()]

#         while stack and curheight == heights[stack[-1]]:
#             stack.pop()

#         if len(stack) > 0:
#             curwidth = n - stack[-1] - 1
#         else:
#             curwidth = n
#         res = max(res, curheight * curwidth)
#     return res

# def largestRectangleArea(self, heights: List[int]) -> int:
#     ##2.单调栈
#     n = len(heights)
#     left, right = [0] * n, [0] * n

#     mnstack = []
#     for i in range(n):
#         while mnstack and heights[i] <= heights[mnstack[-1]]:
#             mnstack.pop()

#         left[i] = mnstack[-1] if mnstack else -1
#         mnstack.append(i)

#     mnstack = []

#     for i in range(n - 1, -1, -1):
#         while mnstack and heights[mnstack[-1]] >= heights[i]:
#             mnstack.pop()
#         right[i] = mnstack[-1] if mnstack else n
#         mnstack.append(i)

#     ans = max((right[i] - left[i] - 1) * heights[i]
#               for i in range(n)) if n > 0 else 0

#     return ans
