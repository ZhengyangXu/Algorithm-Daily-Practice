# @before-stub-for-debug-begin
from python3problem242 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter as Counter 
        s_counter = Counter(s)
        t_counter = Counter(t)
        if len(s_counter) != len(t_counter):
            return False
        else:
            if len(s_counter- t_counter) == 0:
                return True
        return False
        
# @lc code=end

