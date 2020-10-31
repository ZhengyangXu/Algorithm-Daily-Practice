#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (66.75%)
# Likes:    686
# Dislikes: 0
# Total Accepted:    64.5K
# Total Submissions: 96.6K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
# 
# 
# 
# 示例：
# 
# 输入：3
# 输出：
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 8
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:## 带memo的递归
        
        def gt(s,e):
            
            if s > e:
                return [None,]
            memo = [[None]*(n+1) for _ in range(n+1)]
            
            if memo[s][e] != None:
                return memo[s][e]
            
            ans = []
            
            for i in range(s,e+1):
                left = gt(s,i-1)
                right = gt(i+1,e)
                
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l 
                        root.right = r 
                        ans.append(root)
            
            memo[s][e] = ans 
            return ans
            
        return gt(1,n) if n else []
             
                  
        
        
     
                        
        
# @lc code=end

# class Solution:
#     def generateTrees(self, n: int) -> List[TreeNode]: ## 回溯
        
#         def backtrack(path,n):
#             if len(path) == n:
#                 path = path[:]
#                 ans.append(path)
            
            
#             for i in range(1,n+1):
#                 node = TreeNode(i)
                
#                 if node in path:
#                     continue  
#                 if path:
#                     if i > path[-1].val:
#                         path[-1].right = node
#                     else:
#                         path[-1].left = node
                
#                 path.append(node)
#                 backtrack(path,n)
#                 path.pop()
#         ans = []
#         path = []
#         backtrack(path,n)
#         return ans 


## 思路：回溯超时了，这里没有写完。就是把所有节点加入ans，然后遍历ans，这里就写到ans。



    # def generateTrees(self, n: int) -> List[TreeNode]:## 递归  
    #     def gt(start,end):
    #         if start > end:
    #             return [None,]
    #         ans = []
    #         for i in range(start,end+1):
                
    #             left = gt(start,i-1)  
    #             right = gt(i+1,end)
                
    #             for lt in left:
    #                 for rt in right:
    #                     root = TreeNode(i)
    #                     root.left = lt  
    #                     root.right = rt   
    #                     ans.append(root)
    #         return ans    
        
        
    #     return gt(1,n) if n else []     
    
    
        # def generateTrees(self, n: int) -> List[TreeNode]:## 带memo的递归
        
        # def gt(s,e):
            
        #     if s > e:
        #         return [None,]
        #     memo = [[None]*(n+1) for _ in range(n+1)]
            
        #     if memo[s][e] != None:
        #         return memo[s][e]
            
        #     ans = []
            
        #     for i in range(s,e+1):
        #         left = gt(s,i-1)
        #         right = gt(i+1,e)
                
        #         for l in left:
        #             for r in right:
        #                 root = TreeNode(i)
        #                 root.left = l 
        #                 root.right = r 
        #                 ans.append(root)
            
        #     memo[s][e] = ans 
        #     return ans
            
        # return gt(1,n) if n else []