#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#
# https://leetcode-cn.com/problems/grumpy-bookstore-owner/description/
#
# algorithms
# Medium (58.23%)
# Likes:    124
# Dislikes: 0
# Total Accepted:    27.9K
# Total Submissions: 47.9K
# Testcase Example:  '[1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3'
#
# 今天，书店老板有一家店打算试营业 customers.length
# 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
# 
# 在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
# 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
# 
# 书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
# 
# 请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
# 
# 
# 示例：
# 
# 输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# 输出：16
# 解释：
# 书店老板在最后 3 分钟保持冷静。
# 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= X <= customers.length == grumpy.length <= 20000
# 0 <= customers[i] <= 1000
# 0 <= grumpy[i] <= 1
# 
# 
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:  ##常规
        
        n = len(customers)
        total = sum([customers[i] for i in range(n) if grumpy[i] == 0])
        
        increase = sum((customers[i] * grumpy[i] for i in range(X)))
        maxincrease = increase
        for i in range(X,n):
            increase = increase + customers[i] * grumpy[i] - customers[i-X]*grumpy[i-X]
            maxincrease = max(increase,maxincrease)
        
        
        return total + maxincrease 
                
                  
                        
# @lc code=end

    # def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:  ##超时
    #     if not grumpy:
    #         return sum(customers)
    #     interval = [i for i in range(len(grumpy)) if grumpy[i] == 1]
        
    #     ans = 0 
    #     for i in range(len(customers)):
    #         total = sum(customers[i:i+X])
    #         for j in range(len(grumpy)):
    #             if j not in range(i,i+X) and grumpy[j] != 1:
    #                 total += customers[j]
 
                    
    #         ans = max(ans,total)
        
    #     return ans

    # def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:  ##
    #     if not grumpy:
    #         return sum(customers)
    #     total = 0
    #     for i in range(len(customers)):
    #         if grumpy[i] == 0:
    #             total += customers[i]
    #             customers[i] = 0   ## 将grumpy[i]=0的customer置换为0，只需要求X区间内最大值即可
    #     increase = 0 
    #     for i in range(len(customers)):
    #         if i <= len(customers) - X:
    #             increase = max(increase,sum(customers[i:i+X]))
                
        
    #     return total + increase                 
    
    
    思路：1、暴力解法：从头遍历长度为X的区间，算出区间和，区间左边，区间右边依次算出grumpy为0的时候的和。超时
         2、滑动窗口：分为两部分之和，一为grumpy本来就为0之和，为total，接着遍历长度为X的区间，向右滑动时，如果
         滑出区间的grumpy为1，则减去该值，如果滑入区间的grumpy为1，则加上改值，算出最大的increase，加上total即为
         答案。两个技巧:1、算出total后，可以直接把grumpy为0的custumer置为0，这样只用遍历X长度的区间，求出最大值即可
         2、可以用grumpy[i]*customers[i]，直接加上即可，grumpy为0时就为0