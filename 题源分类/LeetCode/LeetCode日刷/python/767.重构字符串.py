#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#
# https://leetcode-cn.com/problems/reorganize-string/description/
#
# algorithms
# Medium (47.67%)
# Likes:    331
# Dislikes: 0
# Total Accepted:    37.7K
# Total Submissions: 79K
# Testcase Example:  '"aab"'
#
# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
# 
# 若可行，输出任意可行的结果。若不可行，返回空字符串。
# 
# 示例 1:
# 
# 
# 输入: S = "aab"
# 输出: "aba"
# 
# 
# 示例 2:
# 
# 
# 输入: S = "aaab"
# 输出: ""
# 
# 
# 注意:
# 
# 
# S 只包含小写字母并且长度在[1, 500]区间内。
# 
# 
#

# @lc code=start
class Solution:
    import heapq 
    def reorganizeString(self, s: str) -> str:
        if not s:
            return True 
        n = len(s)
        count = Counter(s)
        maxCount = max(count.items(),key=lambda x:x[1])[1]
        if maxCount > (n+1) // 2:
            return ''
        q = [(-x[1],x[0]) for x in count.items()]
        heapq.heapify(q)
        ans = []
        
        while len(q) > 1:
            letter1 = heapq.heappop(q)[1]
            letter2 = heapq.heappop(q)[1]
            ans.extend([letter1,letter2])
            count[letter1] -= 1 
            count[letter2] -= 1 
            if count[letter1] > 0:
                heapq.heappush(q,(-count[letter1],letter1))
            if count[letter2] > 0:
                heapq.heappush(q,(-count[letter2],letter2))
        if q: 
            ans.append(q[0][1])
        return "".join(ans)
# @lc code=end

