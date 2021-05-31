#
# @lc app=leetcode.cn id=1074 lang=python3
#
# [1074] 元素和为目标值的子矩阵数量
#
# https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target/description/
#
# algorithms
# Hard (50.41%)
# Likes:    135
# Dislikes: 0
# Total Accepted:    10.6K
# Total Submissions: 16.8K
# Testcase Example:  '[[0,1,0],[1,1,1],[0,1,0]]\n0'
#
# 给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。
# 
# 子矩阵 x1, y1, x2, y2 是满足 x1  且 y1  的所有单元 matrix[x][y] 的集合。
# 
# 如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 !=
# x1'），那么这两个子矩阵也不同。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# 输出：4
# 解释：四个只含 0 的 1x1 子矩阵。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,-1],[-1,1]], target = 0
# 输出：5
# 解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [[904]], target = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# -1000 
# -10^8 
# 
# 
#

# @lc code=start
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        
        def subK(nums,k):
            mp = {0:1}
            n = len(nums)
            count = 0
            pre = 0 
            for i in range(n):
                pre += nums[i] 
                if pre - k in mp:
                    count += mp[pre-k]
                mp[pre] = mp[pre] + 1 if pre in mp else 1 


            
# @lc code=end

    # def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     ans = 0
    #     for i in range(1, n + 1):
    #         presum = [0] * (m + 1)
    #         for j in range(i, n + 1):
    #             a = 0
    #             d = {0:1}
    #             for fixed in range(1, m + 1):
    #                 presum[fixed] += matrix[fixed-1][j-1]
    #                 a += presum[fixed]
    #                 if a - target in d:
    #                     ans += d[a - target]
    #                 if a in d:
    #                     d[a] += 1
    #                 else:
    #                     d[a] = 1
    #     return ans
    
    # def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     ans = 0
    #     presum = [[0]*(n+1) for _ in range(m+1)]
        
    #     for i in range(1,m+1):
    #         for j in range(1,n+1):
    #             presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + matrix[i-1][j-1]
                
    #     for top in range(1,m+1):
    #         for bot in range(top,m+1):
    #             cur = 0 
    #             dic = Counter() 
    #             for r in range(1,n+1):
    #                 cur = presum[bot][r] - presum[top-1][r]
    #                 if cur == target:
    #                     ans += 1 
    #                 if cur - target in dic:
    #                     ans += dic[cur-target]
    #                 dic[cur] += 1 
    #     return ans 
