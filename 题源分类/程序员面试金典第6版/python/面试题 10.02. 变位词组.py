# 面试题 10.02. 变位词组
# 编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

# 注意：本题相对原题稍作修改

# 示例:

# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：

# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 通过次数29,538提交次数40

from collections import defaultdict


def groupAnagrams(strs):
    ans = defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))
        ans[key].append(st)
    return list(ans.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))