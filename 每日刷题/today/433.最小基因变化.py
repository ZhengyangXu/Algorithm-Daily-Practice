#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
# https://leetcode-cn.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (53.51%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    34.3K
# Total Submissions: 63K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# 基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。
#
# 假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。
#
#
# 例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
#
#
# 另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。
#
# 给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end
# 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。
#
# 注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。
#
#
#
# 示例 1：
#
#
# 输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# 输出：1
#
#
# 示例 2：
#
#
# 输入：start = "AACCGGTT", end = "AAACGGTA", bank =
# ["AACCGGTA","AACCGCTA","AAACGGTA"]
# 输出：2
#
#
# 示例 3：
#
#
# 输入：start = "AAAAACCC", end = "AACCCCCC", bank =
# ["AAAACCCC","AAACCCCC","AACCCCCC"]
# 输出：3
#
#
#
#
# 提示：
#
#
# start.length == 8
# end.length == 8
# 0 <= bank.length <= 10
# bank[i].length == 8
# start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成
#
#
#


# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = collections.deque()
        queue.append((start, 0))

        while queue:
            gene, res = queue.popleft()
            if gene == end:
                return res

            for i in range(len(gene)):
                for j in "ACGT":
                    alter = gene[:i] + j + gene[i + 1:]
                    if alter in bank and alter != gene:
                        queue.append((alter, res + 1))
                        bank.remove(alter)

        return -1


# @lc code=end

# def minMutation(self, start: str, end: str, bank: List[str]) -> int: BFS暴力解法
#     def helper(g1, g2):   可优化
#         if not g1 or not g2:
#             return False
#         if len(g1) != len(g2):
#             return False
#         count = 0
#         for i in range(len(g1)):
#             if g1[i] != g2[i]:
#                 count += 1
#         return count == 1

#     queue = [(start, 0)]
#     visited = [start]

#     while queue:
#         g, res = queue.pop(0)
#         if g == end:
#             return res

#         for gene in bank:
#             if helper(g, gene) and gene not in visited:
#                 queue.append((gene, res + 1))
#                 visited.append(gene)

#     return -1
