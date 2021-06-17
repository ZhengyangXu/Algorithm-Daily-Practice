# 第 68 题：树中两个节点的最近公共祖先
# 传送门：树中两个结点的最低公共祖先。

# 给出一个二叉树，输入两个树节点，求它们的最低公共祖先。

# 一个树节点的祖先节点包括它本身。

# 注意：

# 输入的二叉树不为空；
# 输入的两个节点一定不为空，且是二叉树中的节点；
# 样例：

# 二叉树 [8, 12, 2, null, null, 6, 4, null, null, null, null] 如下图所示： 8 / \ 12 2 / \ 6 4 1. 如果输入的树节点为 2 和 12，则输出的最低公共祖先为树节点 8 。

# 如果输入的树节点为 2 和 6 ，则输出的最低公共祖先为树节点 2 。
# 同 LeetCode 第 236 题：二叉树的最近公共祖先。

# 传送门：236. 二叉树的最近公共祖先。

# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

# 《剑指 Offer （第 2 版）》第 68 题：树中两个节点的最近公共祖先-1

# 示例 1:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 输出: 3 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

# 示例 2:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 输出: 5 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

# 说明:

# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        if root == p or root == q:
            return root 
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if not left:
            return right 
        
        if not right:
            return left 
        
        return root 
    
    
    