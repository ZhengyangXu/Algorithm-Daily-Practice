#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (43.49%)
# Likes:    721
# Dislikes: 0
# Total Accepted:    170.5K
# Total Submissions: 391.1K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 
# 
# 示例 1:
# 
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
# 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
# 
# 
# 
# 提示：
# 
# 
# intervals[i][0] <= intervals[i][1]
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        
        for l,r in intervals:
            if not res or  l > res[-1][1]:
                res.append([l,r])
            else:
                res[-1][1] = max(r,res[-1][1])  
        return res 

# @lc code=end

    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     intervals.sort(key=lambda x:x[0])
    #     res = []
        
    #     for l,r in intervals:
    #         if len(res) == 0 or l > res[-1][1]:
    #             res.append([l,r])
    #         else:
    #             res[-1][0],res[-1][1] = min(l,res[-1][0]),max(r,res[-1][1])
                
    #     return res 