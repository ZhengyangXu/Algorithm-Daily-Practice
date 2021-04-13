#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (56.28%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    49.6K
# Total Submissions: 84.5K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#
# 注意：本题与
# 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# 相同
#
#
#
#
#
# 示例 1：
#
#
# 输入：root = [4,2,6,1,3]
# 输出：1
#
#
# 示例 2：
#
#
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [2, 100] 内
# 0
#
#
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
    def minDiffInBST(self, root: TreeNode) -> int: ## 只保存最小当前节点he前一个节点的差值
        stack = []
        node = root
        prev = None
        mindiff = float('inf') 
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev:
                    mindiff = min(node.val-prev.val,mindiff)
                prev = node
                node = node.right

        
        return mindiff 
    
            

# @lc code=end
    # def minDiffInBST(self, root: TreeNode) -> int: ## 数组保存中序遍历结果,时间复杂度o(n),空间消耗大

    #     stack = []
    #     res = []

    #     node = root

    #     while node or stack:
    #         if node:
    #             stack.append(node)
    #             node = node.left
    #         else:
    #             node = stack.pop()
    #             res.append(node)
    #             node = node.right
    #     # mindiff  = float('inf')
    #     # for i in range(1,len(res)):
    #     #     mindiff = min(mindiff,res[i].val-res[i-1].val)
        
    #     return min(res[i].val-res[i-1].val for i in range(1,len(res)))