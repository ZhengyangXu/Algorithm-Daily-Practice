#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (64.41%)
# Likes:    347
# Dislikes: 0
# Total Accepted:    71.4K
# Total Submissions: 110.8K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 示例:
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        cur = [root]
        
        while cur:  
            next = []
            temp = [] 
            for node in cur:
                temp.append(node.val)  
                if node.left:
                    
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            
            ans.append(temp[-1]) 
            cur = next
        return ans 
                
# @lc code=end

