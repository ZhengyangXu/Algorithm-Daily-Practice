#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#
# https://leetcode-cn.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (54.33%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 22.2K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
# 
# 两棵树重复是指它们具有相同的结构以及相同的结点值。
# 
# 示例 1：
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# 
# 下面是两个重复的子树：
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# 
# 和
# 
# ⁠   4
# 
# 
# 因此，你需要以列表的形式返回上述重复子树的根结点。
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
    import collections 
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]: ## 官方题解 UID
        counter = collections.Counter()
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        ans = []
        def traverse(root):
            if not root:
                return "#"
            uid = trees[root.val,traverse(root.left),traverse(root.right)]
            counter[uid] += 1  
            if counter[uid] == 2:
                ans.append(root)
              
        traverse(root)
        
        return ans 
        
# # @lc code=end
#     def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]: ## 递归
#         counter = collections.Counter()
#         ans = []
#         def traverse(root):
#             if not root:
#                 return "#"
#             subtree = "{},{},{}".format(root.val,traverse(root.left),traverse(root.right))
#             counter[subtree] += 1  
#             if counter[subtree] == 2:
#                 ans.append(root)
#             return subtree  
#         traverse(root)
        
#         return ans 
