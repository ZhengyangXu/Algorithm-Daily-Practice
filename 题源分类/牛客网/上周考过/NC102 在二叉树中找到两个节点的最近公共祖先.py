# NC102 在二叉树中找到两个节点的最近公共祖先
# 题目
# 题解(143)
# 讨论(149)
# 排行
# 中等  通过率：47.56%  时间限制：1秒  空间限制：256M
# 知识点
# 树
# 描述
# 给定一棵二叉树(保证非空)以及这棵树上的两个节点对应的val值 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。

# 数据范围：树上节点数满足 1 \le n \le 10^5 \1≤n≤10
# 5
#    , 节点值val满足区间 [0,n)
# 要求：时间复杂度 O(n)O(n)

# 注：本题保证二叉树中每个节点的val值均不相同。

# 如当输入{3,5,1,6,2,0,8,#,#,7,4},5,1时，二叉树{3,5,1,6,2,0,8,#,#,7,4}如下图所示：

# 所以节点值为5和节点值为1的节点的最近公共祖先节点的节点值为3，所以对应的输出为3。
# 节点本身可以视为自己的祖先
# 示例1
# 输入：
# {3,5,1,6,2,0,8,#,#,7,4},5,1
# 复制
# 返回值：
# 3
# 复制
# 示例2
# 输入：
# {3,5,1,6,2,0,8,#,#,7,4},2,7
# 复制
# 返回值：
# 2


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, o1: int, o2: int) -> int:
        def dfs(root, o1, o2):
            if not root:
                return None  #
            if root.val == o1 or root.val == o2:
                return root
            left = dfs(root.left, o1, o2)
            right = dfs(root.right, o1, o2)
            if not left:
                return right
            if not right:
                return left
            return root

        return dfs(root, o1, o2).val

        # write code here
    def lowestCommonAncestor2(self, root: TreeNode, o1: int, o2: int) -> int:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)

        if not left:
            return right
        if not right:
            return left
        return root
