#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
# https://leetcode-cn.com/problems/candy/description/
#
# algorithms
# Hard (48.10%)
# Likes:    447
# Dislikes: 0
# Total Accepted:    59.9K
# Total Submissions: 124.5K
# Testcase Example:  '[1,0,2]'
#
# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
# 
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
# 
# 
# 每个孩子至少分配到 1 个糖果。
# 评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
# 
# 
# 那么这样下来，老师至少需要准备多少颗糖果呢？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[1,0,2]
# 输出：5
# 解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
# 
# 
# 示例 2：
# 
# 
# 输入：[1,2,2]
# 输出：4
# 解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
# ⁠    第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
# 
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        n = len(ratings)
        ret = 1 
        pre,inc,dec = 1,1,0
        
        for i in range(1,n):
            if ratings[i] >= ratings[i-1]:
                dec = 0 
                pre = 1 if ratings[i-1] == ratings[i] else pre + 1
                ret += pre 
                inc = pre 
                
            else:
                dec += 1 
                if dec == inc:
                    dec += 1 
                ret += dec 
                pre = 1 
                
        return ret 
            
        
# @lc code=end

    # def candy(self, ratings: List[int]) -> int:
    #     n = len(ratings)
    #     left = [0] * n 
    #     for i in range(n):
    #         if i > 0 and ratings[i] > ratings[i-1]:
    #             left[i] = left[i-1] + 1 
    #         else:
    #             left[i] = 1
                
    #     right = ret = 0 
    #     for i in range(n-1,-1,-1):
    #         if i < n-1 and ratings[i] > ratings[i+1]:
    #             right += 1
    #         else:
    #             right = 1 
    #         ret += max(right,left[i])
            
    #     return ret 
    
    # def candy(self, ratings: List[int]) -> int:
    #     if not ratings:
    #         return 0
    #     n = len(ratings)
    #     candy = [1]*n 
        
    #     for i in range(1,n):
    #         if ratings[i] > ratings[i-1]:
    #             candy[i] = candy[i-1] + 1 
                
    #     for i in range(n-1,0,-1):
    #         if ratings[i-1] > ratings[i]:
    #             candy[i-1] = max(candy[i-1],candy[i]+1)
        
        
    #     return sum(candy)