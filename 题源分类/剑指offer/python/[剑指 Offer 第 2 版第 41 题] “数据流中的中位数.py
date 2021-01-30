# 题目描述
# 如何得到一个数据流中的中位数？

# 如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。

# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

# 样例
# 输入：1, 2, 3, 4

# 输出：1,1.5,2,2.5

# 解释：每当数据流读入一个数据，就进行一次判断并输出当前的中位数。
import heapq
class streamMedian:
    def __init__(self):
        self.count = 0 
        self.minHeap = []
        self.maxHeap = []
    
    def insert1(self,num):
        self.count += 1 
        if self.count % 2 == 0:
            heapq.heappush(self.minHeap,num)
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-temp)
        else:
            heapq.heappush(self.maxHeap,-num)
            temp = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,temp)
    
    def insert2(self,num):
        heapq.heappush(self.minHeap,num)
        temp = heapq.heappop(self.minHeap)
        heapq.heappush(self.maxHeap,-temp)
        if self.count & 1 == 0:
            temp = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,temp)
        self.count += 1 
    
    def getMedian(self):
        if self.count % 2 == 0:
            return (self.minHeap[0]+(-self.maxHeap[0]))/2 
        else:
            return self.minHeap[0]
        
        
    
if __name__ == "__main__":
    
    streamMedian1 = streamMedian() 
    streamMedian1.insert1(1)
    print(streamMedian1.getMedian())
    streamMedian1.insert1(2)
    print(streamMedian1.getMedian())
    streamMedian1.insert1(3)
    print(streamMedian1.getMedian())
    streamMedian1.insert1(4)
    print(streamMedian1.getMedian())
    print(streamMedian1.minHeap)
    # print(streamMedian1.maxHeap)
 

        