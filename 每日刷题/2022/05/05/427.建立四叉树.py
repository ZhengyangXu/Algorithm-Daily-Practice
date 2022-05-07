#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#
# https://leetcode-cn.com/problems/construct-quad-tree/description/
#
# algorithms
# Medium (61.89%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    15.4K
# Total Submissions: 22K
# Testcase Example:  '[[0,1],[1,0]]'
#
# 给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。
#
# 你需要返回能表示矩阵的 四叉树 的根结点。
#
# 注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。
#
# 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：
#
#
# val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
# isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。
#
#
# class Node {
# ⁠   public boolean val;
# public boolean isLeaf;
# public Node topLeft;
# public Node topRight;
# public Node bottomLeft;
# public Node bottomRight;
# }
#
# 我们可以按以下步骤为二维区域构建四叉树：
#
#
# 如果当前网格的值相同（即，全为 0 或者全为 1），将 isLeaf 设为 True ，将 val 设为网格相应的值，并将四个子节点都设为 Null
# 然后停止。
# 如果当前网格的值不同，将 isLeaf 设为 False， 将 val 设为任意值，然后如下图所示，将当前网格划分为四个子网格。
# 使用适当的子网格递归每个子节点。
#
#
#
#
# 如果你想了解更多关于四叉树的内容，可以参考 wiki 。
#
# 四叉树格式：
#
# 输出为使用层序遍历后四叉树的序列化形式，其中 null 表示路径终止符，其下面不存在节点。
#
# 它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 [isLeaf, val] 。
#
# 如果 isLeaf 或者 val 的值为 True ，则表示它在列表 [isLeaf, val] 中的值为 1 ；如果 isLeaf 或者 val 的值为
# False ，则表示值为 0 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[0,1],[1,0]]
# 输出：[[0,1],[1,0],[1,1],[1,1],[1,0]]
# 解释：此示例的解释如下：
# 请注意，在下面四叉树的图示中，0 表示 false，1 表示 True 。
#
#
#
# 示例 2：
#
#
#
# 输入：grid =
# [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
#
# 输出：[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# 解释：网格中的所有值都不相同。我们将网格划分为四个子网格。
# topLeft，bottomLeft 和 bottomRight 均具有相同的值。
# topRight 具有不同的值，因此我们将其再分为 4 个子网格，这样每个子网格都具有相同的值。
# 解释如下图所示：
#
#
#
# 示例 3：
#
# 输入：grid = [[1,1],[1,1]]
# 输出：[[1,1]]
#
#
# 示例 4：
#
# 输入：grid = [[0]]
# 输出：[[1,0]]
#
#
# 示例 5：
#
# 输入：grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
# 输出：[[0,1],[1,1],[1,0],[1,0],[1,1]]
#
#
#
#
# 提示：
#
#
# n == grid.length == grid[i].length
# n == 2^x 其中 0 <= x <= 6
#
#
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        pre = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][
                    j - 1] + grid[i - 1][j - 1]

        def getSum(r0: int, c0: int, r1: int, c1: int) -> int:
            return pre[r1][c1] - pre[r1][c0] - pre[r0][c1] + pre[r0][c0]

        def dfs(r0: int, c0: int, r1: int, c1: int) -> 'Node':
            total = getSum(r0, c0, r1, c1)
            if total == 0:
                return Node(False, True)
            if total == (r1 - r0) * (c1 - c0):
                return Node(True, True)
            return Node(
                True,
                False,
                dfs(r0, c0, (r0 + r1) // 2, (c0 + c1) // 2),
                dfs(r0, (c0 + c1) // 2, (r0 + r1) // 2, c1),
                dfs((r0 + r1) // 2, c0, r1, (c0 + c1) // 2),
                dfs((r0 + r1) // 2, (c0 + c1) // 2, r1, c1),
            )

        return dfs(0, 0, n, n)

    # def construct(self, grid: List[List[int]]) -> 'Node':
    #     n = len(grid)
    #     m = len(grid)
    #     presum = [[0] * (n + 1) for _ in range(m + 1)]
    #     for i in range(m):
    #         for j in range(n):
    #             presum[i + 1][j + 1] += presum[i + 1][j] + presum[i][
    #                 j - 1] - presum[i][j] + grid[i][j]

    #     def dfs(x0, y0, x1, y1):
    #         if not (diff := presum[x1][y1] - presum[x1][y0] - presum[x0][y1] +
    #                 presum[x0][y0]):
    #             return Node(False, True, None, None, None, None)
    #         elif diff == (x1 - x0) * (y1 - y0):
    #             return Node(True, True, None, None, None, None)
    #         else:
    #             # 这里填True、False都行
    #             return Node(
    #                 True, False,
    #                 dfs(x0, y0, hx := (x0 + x1) // 2, hy := (y0 + y1) // 2),
    #                 dfs(x0, hy, hx, y1), dfs(hx, y0, x1, hy),
    #                 dfs(hx, hy, x1, y1))

    #     return dfs(0, 0, m, n)


# @lc code=end
# def dfs(r0, c0, r1, c1):
#     if all(grid[i][j] == grid[r0][c0] for i in range(r0, r1)
#            for j in range(c0, c1)):
#         return Node(grid[r0][c0] == 1, True)
#     return Node(
#         True,
#         False,
#         dfs(r0, c0, (r0 + r1) // 2, (c0 + c1) // 2),
#         dfs(r0, (c0 + c1) // 2, (r0 + r1) // 2, c1),
#         dfs((r0 + r1) // 2, c0, r1, (c0 + c1) // 2),
#         dfs((r0 + r1) // 2, (c0 + c1) // 2, r1, c1),
#     )

# return dfs(0, 0, len(grid), len(grid))

#
