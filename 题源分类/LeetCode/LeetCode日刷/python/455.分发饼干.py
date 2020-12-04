#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        for i in g:
            if i in s:
                res += 1
                s.remove(i)
        return res

        
# @lc code=end

