#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (48.90%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    24.8K
# Total Submissions: 50.5K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
# 
# 例如，
# 
# [2,3,4] 的中位数是 3
# 
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 
# 设计一个支持以下两种操作的数据结构：
# 
# 
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 
# 
# 示例：
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 进阶:
# 
# 
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
# 
# 
#

# @lc code=start
import heapq as hq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.large = []
        self.small = []
        
        

    def addNum(self, num: int) -> None:
      self.count += 1 
      hq.heappush(self.large,(-num,num))
      _,large_top = hq.heappop(self.large)
      hq.heappush(self.small,large_top)
      
      if self.count % 2 != 0:
        small_top = hq.heappop(self.small)
        hq.heappush(self.large,(-small_top,small_top)) 
        

    def findMedian(self) -> float:
      if self.count % 2 != 0:
        return self.large[0][1]
      else:
        return (self.small[0]+self.large[0][1])/2
      
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

