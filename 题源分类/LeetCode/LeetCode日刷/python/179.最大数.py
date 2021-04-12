#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (37.68%)
# Likes:    452
# Dislikes: 0
# Total Accepted:    50.3K
# Total Submissions: 133.4K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。
#
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#
#
# 示例 1：
#
#
# 输入：nums = [10,2]
# 输出："210"
#
# 示例 2：
#
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#
#
# 示例 3：
#
#
# 输入：nums = [1]
# 输出："1"
#
#
# 示例 4：
#
#
# 输入：nums = [10]
# 输出："10"
#
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
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numstr = list(map(str, nums))
        compare = lambda x, y: 1 if x + y < y + x else -1
        numstr.sort(key=functools.cmp_to_key(compare))
        res = "".join(numstr)
        if res[0] == "0":
            res = "0"

        return res


# @lc code=end

# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         if not nums:
#             return ''

#         cmp = cmp_to_key(lambda a,b:int(b+a)-int(a+b))
#         res = sorted(map(str,nums),key=cmp)

#         return ''.join(res) if res[0] != str(0) else '0'