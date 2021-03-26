#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#
# https://leetcode-cn.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (66.36%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    32.3K
# Total Submissions: 45.2K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
# 
# 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
# 
# 
# 
# 示例 1:
# 
# 输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
# 
# 示例 2:
# 
# 输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
# 
# 
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:

                
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [i for i in nestedList[::-1]]
    
    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()
 
        
    def hasNext(self) -> bool:
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True 
            self.stack.pop() 
            for i in range(len(cur.getList())-1,-1,-1):
                self.stack.append(cur.getList()[i])
                
        return False 
        
       
        
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

# class NestedIterator:

                
#     def __init__(self, nestedList: [NestedInteger]):
#         self.queue = []
#         self.dfs(nestedList)
    
    
#     def dfs(self,nested):
#         for nest in nested:
#             if nest.isInteger():
#                 self.queue.append(nest.getInteger())
#             else:
#                 self.dfs(nest.getList())
    
#     def next(self) -> int:
#         return self.queue.pop(0)
        
#     def hasNext(self) -> bool:
#         return len(self.queue) > 0 
        