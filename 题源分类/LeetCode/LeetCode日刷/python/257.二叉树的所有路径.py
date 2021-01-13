#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (66.37%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    91.5K
# Total Submissions: 137.8K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]: ## DFS
        if not root:
            return []
        res = []
        def buildPath(root,path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    res.append(path)
                else:
                    path += "->"
                    buildPath(root.left,path)
                    buildPath(root.right,path)
            
        buildPath(root,"")
        return res  
        

                
                
            
# @lc code=end

    # def binaryTreePaths(self, root: TreeNode) -> List[str]: ## BFS
    #     if not root:
    #         return []

    #     res = []
    #     cur = [(root,str(root.val))]
        
    #     while cur: 
    #         node,path = cur.pop(0)
    #         if not node.left and not node.right:
    #             res.append(path)
    #         if node.left:
    #             cur.append((node.left,path+"->"+str(node.left.val)))
    #         if node.right:
    #             cur.append((node.right,path+"->"+str(node.right.val)))
                


    #     return res 