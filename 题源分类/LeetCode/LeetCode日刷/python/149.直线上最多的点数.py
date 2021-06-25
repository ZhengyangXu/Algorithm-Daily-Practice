#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# https://leetcode-cn.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (25.78%)
# Likes:    300
# Dislikes: 0
# Total Accepted:    34.6K
# Total Submissions: 113.6K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# points[i].length == 2
# -10^4 i, yi 
# points 中的所有点 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        ans = 1 
        for i in range(n):
            dic = dict()
            maxnum = 0 
            for j in range(i+1,n):
                x1,x2,y1,y2 = points[i][0],points[j][0],points[i][1],points[j][1]
                a,b = x1-x2,y1-y2
                # k = math.gcd(a,b)
                # key = f'{a//k}-{b//k}'
                key = b/a if a else inf 
                if key not in dic:
                    dic[key] = 1 
                else:
                    dic[key] += 1 
                maxnum = max(maxnum,dic[key])
            ans = max(ans,maxnum+1)
        return ans 
# @lc code=end

