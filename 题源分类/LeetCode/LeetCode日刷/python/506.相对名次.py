#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
# https://leetcode-cn.com/problems/relative-ranks/description/
#
# algorithms
# Easy (55.70%)
# Likes:    70
# Dislikes: 0
# Total Accepted:    14.8K
# Total Submissions: 26.5K
# Testcase Example:  '[5,4,3,2,1]'
#
# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold
# Medal", "Silver Medal", "Bronze Medal"）。
# 
# (注：分数越高的选手，排名越靠前。)
# 
# 示例 1:
# 
# 
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and
# "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
# 
# 提示:
# 
# 
# N 是一个正整数并且不会超过 10000。
# 所有运动员的成绩都不相同。
# 
# 
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        res = []
        for i in range(len(score)):
            res.append((score[i],i))
            
        res = sorted(res,key=lambda x:x[0],reverse=True)
        
        for i in range(len(score)):
            if i == 0:
                score[res[i][1]] = "Gold Medal"
            elif i == 1:
                score[res[i][1]] = "Silver Medal"
            elif i == 2:
                score[res[i][1]] = "Bronze Medal"
            else:
                score[res[i][1]] = str(i+1)
                
        
        return score
        

        
# @lc code=end

    # def findRelativeRanks(self, score: List[int]) -> List[str]:
        
    #     n = len(score)
    #     res=[0]*n
    #     for i in range(n):
    #         count = 1
    #         for j in range(n):
    #             if score[j] > score[i]:
    #                 count += 1
    #         res[i] = count
            
    #     score = res    
    #     for i in range(n):
    #         if score[i] == 1:
    #             score[i] = "Gold Medal"
    #         elif score[i] == 2:
    #             score[i] = "Silver Medal"
    #         elif score[i] == 3:
    #             score[i] = "Bronze Medal"
    #         else:
    #             score[i] = str(score[i])    
                
    #     return score

## 思路：1、记录原数组的index后排序，排序后的数组就是真正的排名，然后按照原来的index还原
##      2、记录大于list里出自己外的个数，就是排名，然后转换