#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.13%)
# Likes:    1315
# Dislikes: 0
# Total Accepted:    180.1K
# Total Submissions: 236.3K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#

# @lc code=start
class Solution:  ### 动态规划
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        dp = [None for _ in range(n+1)]
        dp[0] = [""]
        
        for i in range(1,n+1):
            cur = []
            for j in range(i):
                left = dp[j] 
                right = dp[i-j-1]
                for s1 in left:
                    for s2 in right:
                        cur.append("("+s1+")"+s2)
            dp[i] = cur  
        return dp[n]

                
            

# @lc code=end
    # def generateParenthesis(self, n: int) -> List[str]:
    #     def dfs(path,left,right):
    #         if left == 0 and right == 0:
    #             res.append(path)
    #             return 
    #         if right < left:
    #             return 
    #         if left > 0:
    #             dfs(path+'(',left-1,right)
    #         if right > 0:
    #             dfs(path+')',left,right-1)
    #     path = ''
    #     res = []
    #     dfs(path,n,n)
    #     return res



        # def dfs(path,left,right,n):
        #     if left == n and right == n:
        #         res.append(path)
        #         return 
        #     if left < right:
        #         return   
        #     if left < n:
        #         dfs(path+'(',left+1,right,n)
        #     if right < n:
        #         dfs(path+')',left,right+1,n)
        # res = []
        # path = ''
        # dfs(path,0,0,n)

        # return res 



        # def backtrack(path,left,right,n):
        #     if len(path) == 2*n:
        #         res.append(path)
        #         return  
        #     if right > left:
        #         return 
        #     if left < n:
        #         path += '('
        #         backtrack(path,left+1,right,n)
        #         path = path[:-1]
        #     if right < n:
        #         path += ')'
        #         backtrack(path,left,right+1,n)
        #         path = path[:-1]
        # res = []
        # path = ''
        # backtrack(path,0,0,n)
        # return res   
        
        
        
#### 回溯和递归一直搞不清楚。尤其是两种写法，一种有pop，也就是回复现场，一种没有，就是直接在递归函数里
#### 更新条件。前者更容易理解。