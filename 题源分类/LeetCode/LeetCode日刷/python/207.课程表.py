#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (54.46%)
# Likes:    651
# Dislikes: 0
# Total Accepted:    84.6K
# Total Submissions: 155.3K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
# 
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
# 
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
# 
# 
# 
# 示例 1:
# 
# 输入: 2, [[1,0]] 
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
# 
# 示例 2:
# 
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
# 
# 
# 
# 提示：
# 
# 
# 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 1 <= numCourses <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if len(prerequisites) == 0:
            return True  
        adj = [set() for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        def dfs(course,adj,visited):
            if visited[course] == -1:
                return True 
            if visited[course] == 1:
                return False 
            visited[course] = 1  
            
            for after in adj[course]:
                if not dfs(after,adj,visited):
                    return False 
                
            visited[course] =-1 
            return True 
        
        for after,before in prerequisites:
            adj[before].add(after)
        
        for i in range(numCourses):
            if not dfs(i,adj,visited):
                return False 
        
        return True 
                    
                    
            
        

        
# @lc code=end

    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: bfs
        
    #     size = numCourses
    #     if size == 0:
    #         return True  
        
    #     indegrees = [0 for _ in range(size)]
    #     adj = [set() for _ in range(size)]
        
        
    #     for after,before in prerequisites:
    #         indegrees[after] += 1  
    #         adj[before].add(after)
            
    #     que = []
        
    #     for i in range(len(indegrees)):
    #         if indegrees[i] == 0:
    #             que.append(i)
        
    #     count = 0
                
    #     while que:
    #         top = que.pop(0)
    #         count += 1 
    #         for after in adj[top]:
    #             indegrees[after] -= 1 
    #             if indegrees[after] == 0:
    #                 que.append(after)
                    
    #     return count == size
    
    
    #  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: ## bfs
        
    #     if len(prerequisites) == 0:
    #         return True 
    #     valid = True 
    #     visited = [0 for _ in range(numCourses)]
    #     adj = [set() for _ in range(numCourses)]
        
    #     for after,before in prerequisites:
    #         adj[before].add(after)
    #     result = []
    #     def dfs(course):
    #         nonlocal valid 
    #         visited[course] = 1
            
    #         for after in adj[course]:
    #             if visited[after] == 0:
    #                 dfs(after)
    #                 if not valid:
    #                     return 
    #             elif visited[after] == 1:
    #                 valid = False 
    #                 return 
                
    #         visited[course] = -1 
    #         result.append(course)
        
    #     for course in range(numCourses):
    #         if valid and not visited[course]:
    #             dfs(course)
                
    #     return valid 
                    