#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (78.43%)
# Likes:    275
# Dislikes: 0
# Total Accepted:    55K
# Total Submissions: 70.1K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 
# 示例:
# 
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return 
        
        m = n * n 
        q = 1
        res = [[0]*n for _ in range(n)]
        bottom,top,left,right = 0,n,0,n
        while q <= m and bottom < top and left < right:
            for i in range(left,right):
                res[bottom][i] = q 
                q += 1 
            
            bottom += 1 
            
            for i in range(bottom,top):
                res[i][right-1] = q  
                q += 1 
            
            right -= 1 
            
            for i in range(right-1,left-1,-1):
                res[top-1][i] = q 
                q += 1  
            top -= 1  
            
            for i in range(top-1,bottom-1,-1):
                res[i][left] = q  
                q += 1 
            left += 1 
            
        return res 
                
            
# @lc code=end

