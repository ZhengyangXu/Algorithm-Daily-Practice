#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#
# https://leetcode-cn.com/problems/flipping-an-image/description/
#
# algorithms
# Easy (75.79%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    67.6K
# Total Submissions: 85.2K
# Testcase Example:  '[[1,1,0],[1,0,1],[0,0,0]]'
#
# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
# 
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
# 
# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[[1,1,0],[1,0,1],[0,0,0]]
# 输出：[[1,0,0],[0,1,0],[1,1,1]]
# 解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
# ⁠    然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
# ⁠    然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        
        ## 一行 
        
        # return [[x ^ 1 for x in row[::-1]] for row in A]
        
        # return [[1-x for x in row[::-1]] for row in A]
        
        
        return [[1-A[i][len(A[i])-1-j] for i in range(len(A))] for j in range(len(A))]
                
        
# @lc code=end

    # def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
    #     n = len(A)
    #     N = len(A[0])

        
    #     for i in range(n):
    #         for j in range((N+1)//2):
    #             A[i][j],A[i][N-j-1] = 1-A[i][N-j-1],1-A[i][j]
                
        
        
    #     return A
    
    
        # def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        # n = len(A)
        # N = len(A[0])

        
        # for row in A:
        #     left,right = 0,len(row)-1
        #     while left < right:
        #         if row[left] == row[right]:
        #             row[left] ^= 1
        #             row[right] ^= 1
        #         left += 1
        #         right -= 1
            
        #     if left == right:
        #         row[left] ^= 1
                
        
        
        # return A
        
        
        
    # def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
    #     n = len(A)
    #     m = len(A[0])
    #     res = [[0]*m for _ in range(n)]
        
    #     for i in range(n):
    #         for j in range(m):
    #             res[i][j] = 1 - A[i][m-1-j]
                
    #     return res 