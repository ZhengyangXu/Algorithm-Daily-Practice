#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (64.66%)
# Likes:    1300
# Dislikes: 0
# Total Accepted:    556K
# Total Submissions: 859.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
#
#
# 示例 2：
#
#
# 输入：root = [1]
# 输出：[[1]]
#
#
# 示例 3：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        

 
        # queue = [root] 
        # while queue:
        #     tmp = [] 
        #     size = len(queue ) 
        #     for  _ in range(size):
        #         node = queue.pop(0)
        #         tmp.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
                    
        #     res.append(tmp)
        # return res  
            
             
        # res = []
        # if not root:
        #     return res
        # cur = [root]
        # while cur:
        #     next_layer = []
        #     cur_layer = []
        #     for node in cur:
        #         if node.left:
        #             next_layer.append(node.left)
        #         if node.right:
        #             next_layer.append(node.right)
        #         cur_layer.append(node.val)
        #     res.append(cur_layer)
        #     cur = next_layer
        # return res