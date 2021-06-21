#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#
# https://leetcode-cn.com/problems/smallest-good-base/description/
#
# algorithms
# Hard (43.55%)
# Likes:    103
# Dislikes: 0
# Total Accepted:    9.5K
# Total Submissions: 17K
# Testcase Example:  '"13"'
#
# 对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。
#
# 以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。
#
#
#
# 示例 1：
#
#
# 输入："13"
# 输出："3"
# 解释：13 的 3 进制是 111。
#
#
# 示例 2：
#
#
# 输入："4681"
# 输出："8"
# 解释：4681 的 8 进制是 11111。
#
#
# 示例 3：
#
#
# 输入："1000000000000000000"
# 输出："999999999999999999"
# 解释：1000000000000000000 的 999999999999999999 进制是 11。
#
#
#
#
# 提示：
#
#
# n的取值范围是 [3, 10^18]。
# 输入总是有效且没有前导 0。
#
#
#
#
#


# @lc code=start
class Solution:
    import math
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        # n = x^(m-1) + x^(m-2) + ... + x + 1
        for m in range(num.bit_length(),2,-1):
            # 二项式展开 x^(m-1) < n < (x+1)^(m-1)
            x = int(pow(num,1/(m-1)))
            # 等比数列求和 n = (x^m - 1)/(x-1)
            if num == (pow(x,m) - 1)//(x-1):
                return str(x)
        return str(num-1)



# @lc code=end

    def smallestGoodBase(self, n: str) -> str:
        def toK(n, k):
            if not n:
                return
            ans = []
            while n:
                n, r = divmod(n, k)
                ans.append(n % k)
            return ans

        for i in range(2, int(n) - 1):
            ans = toK(int(n), i)
            if all(map(lambda x: x == 1, ans)):
                return str(i)