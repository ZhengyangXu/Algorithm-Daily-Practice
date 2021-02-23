#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
# https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (49.99%)
# Likes:    270
# Dislikes: 0
# Total Accepted:    47.9K
# Total Submissions: 95.8K
# Testcase Example:  '[1,null,2,2]'
#
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
#
# 假定 BST 有如下定义：
#
#
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
#
#
# 例如：
# 给定 BST [1,null,2,2],
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
#
#
# 返回[2].
#
# 提示：如果众数超过1个，不需考虑输出顺序
#
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
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
    def findMode(self, root: TreeNode) -> List[int]:
        self.pre = None
        self.count = self.maxcount = 0
        self.result = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)

            if not self.pre:
                self.count = 1
            elif self.pre.val == root.val:
                self.count += 1
            else:
                self.count = 1
            self.pre = root

            if self.count == self.maxcount:
                self.result.append(root.val)

            if self.count > self.maxcount:
                self.maxcount = self.count
                self.result = []
                self.result.append(root.val)

            dfs(root.right)
            return

        dfs(root)

        return self.result


# @lc code=end
