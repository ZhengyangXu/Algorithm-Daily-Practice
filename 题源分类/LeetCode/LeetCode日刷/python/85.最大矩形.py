#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (51.60%)
# Likes:    809
# Dislikes: 0
# Total Accepted:    67K
# Total Submissions: 129.8K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = []
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：matrix = [["1"]]
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：matrix = [["0","0"]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# rows == matrix.length
# cols == matrix[0].length
# 0 
# matrix[i][j] 为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0 
        
        n = len(matrix[0])
        height = [0] * (n+1)
        ans = 0 
        
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0 
            stack = [-1]
            
            for i in range(n+1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans,h*w)
                stack.append(i)
        return ans 
                    
# @lc code=end

    # def maximalRectangle(self, matrix: List[List[str]]) -> int:
    #     if not matrix or not matrix[0]:
    #         return 0 
        
    #     n = len(matrix[0])
    #     height = [0] * (n+1)
    #     ans = 0 
        
    #     for row in matrix:
    #         for i in range(n):
    #             height[i] = height[i] + 1 if row[i] == '1' else 0 
    #         stack = [-1]
            
    #         for i in range(n+1):
    #             while height[i] < height[stack[-1]]:
    #                 h = height[stack.pop()]
    #                 w = i - 1 - stack[-1]
    #                 ans = max(ans,h*w)
    #             stack.append(i)
    #     return ans 