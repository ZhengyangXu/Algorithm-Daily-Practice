#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (39.90%)
# Likes:    336
# Dislikes: 0
# Total Accepted:    57.9K
# Total Submissions: 144.9K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 
# 
# 
# 示例 1：
# 
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 
# 
# 示例 2：
# 
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 
# 
# 
# 
# 注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。
# 
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newl,newr = newInterval[0],newInterval[1]
        
        size = len(intervals)
        i = 0 
        while i < size and intervals[i][1] < newl:
            res.append(intervals[i])
            i += 1 
        while i < size and intervals[i][0] <= newr:
            newl,newr = min(intervals[i][0],newl),max(intervals[i][1],newr)
            i += 1 
        res.append([newl,newr])
        while i < size:
            res.append(intervals[i])
            i += 1
        
        return res     
        
                
# @lc code=end

    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     size = len(intervals)
    #     if size == 0:
    #         return [newInterval]
    #     merged = [0 for _ in range(size)]
    #     for i in range(size):
    #         low,high = intervals[i][0],intervals[i][1]
    #         newlow,newhigh = newInterval[0],newInterval[1]
    #         if high < newlow or low > newhigh:
    #             merged[i] = -1 
    #         else:
    #             merged[i] = 1  
    #             intervals[i][0],intervals[i][1] = min(low,newlow),max(high,newhigh)
    #             newInterval[0],newInterval[1] = min(low,newlow),max(high,newhigh)  
                
    #     res = []
    #     for i in range(size):
    #         if merged[i] == -1:
    #             res.append(intervals[i])
    #         if merged[i] == False or  (merged[i] == True and i + 1 == size) or (merged[i] == True and merged[i+1] == False):
    #             res.append(intervals[i])
                
    #     return res 
    
    
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     newlow,newhigh = newInterval[0],newInterval[1]
    #     placed = False 
    #     res = []
    #     for low,high in intervals:
    #         if low > newhigh:
    #             if not placed:
    #                 res.append([newlow,newhigh])
    #                 placed = True  
    #             res.append([low,high])
    #         elif high < newlow:
    #             res.append([low,high])
                
    #         else:
    #             newlow = min(newlow,low)
    #             newhigh = max(newhigh,high)
                
    #     if not placed:
    #         res.append([newlow,newhigh])
            
    #     return res     