#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#
# https://leetcode-cn.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (51.13%)
# Likes:    442
# Dislikes: 0
# Total Accepted:    25.4K
# Total Submissions: 49.6K
# Testcase Example:  '"()())()"'
#
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
# 
# 返回所有可能的结果。答案可以按 任意顺序 返回。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "()())()"
# 输出：["(())()","()()()"]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "(a)())()"
# 输出：["(a())()","(a)()()"]
# 
# 
# 示例 3：
# 
# 
# 输入：s = ")("
# 输出：[""]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由小写英文字母以及括号 '(' 和 ')' 组成
# s 中至多含 20 个括号
# 
# 
#
# class Solution {
#     int len;
#     public List<String> removeInvalidParentheses(String s) {
#         char[] cs = s.toCharArray();
#         int l = 0, r = 0;
#         for (char c : cs) {
#             if (c == '(') {
#                 l++;
#             } else if (c == ')') {
#                 r++;
#             }
#         }
#         int max = Math.min(l, r);
#         Set<String> all = new HashSet<>();
#         dfs(cs, 0, 0, max, "", all);
#         List<String> ans = new ArrayList<>();
#         for (String str : all) {
#             if (str.length() == len) ans.add(str);
#         }
#         return ans;
#     }
#     /**
#      * cs: 字符串 s 对应的字符数组
#      * u: 当前决策到 cs 的哪一位
#      * score: 当前决策方案的得分值（每往 cur 追加一个左括号进行 +1；每往 cur 追加一个右括号进行 -1）
#      * max: 整个 dfs 过程的最大得分
#      * cur: 当前决策方案 
#      * ans: 合法方案结果集
#      */
#     void dfs(char[] cs, int u, int score, int max, String cur, Set<String> ans) {
#         if (u == cs.length) {
#             if (score == 0 && cur.length() >= len) {
#                 len = Math.max(len, cur.length());
#                 ans.add(cur);
#             }
#             return;
#         }
#         if (cs[u] == '(') {
#             if (score + 1 <= max) dfs(cs, u + 1, score + 1, max, cur + "(", ans);
#             dfs(cs, u + 1, score, max, cur, ans);
#         } else if (cs[u] == ')') {
#             if (score > 0) dfs(cs, u + 1, score - 1, max, cur + ")", ans);
#             dfs(cs, u + 1, score, max, cur, ans);
#         } else {
#             dfs(cs, u + 1, score, max, cur + String.valueOf(cs[u]), ans);
#         }
#     }
# }


# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        valid = []
        length = len(s)
        l,r = 0,0 
        for char in s:
            if char == "(":
                l += 1 
            elif char == ")":
                if l == 0:
                    r += 1 
                if l > 0:
                    l -= 1 
        
        
        def dfs(index,leftcount,rightcount,leftremove,rightremove, path):
            if index == length:
                if leftremove == 0 and rightremove == 0:
                    path = path[:]
                    if path not in valid:
                        valid.append(path)
                return 
            char = s[index]
            
            if char == "(" and leftremove > 0:
                dfs(index+1,leftcount,rightcount,leftremove-1,rightremove,path)
            
            if char == ")" and rightremove > 0:
                dfs(index+1,leftcount,rightcount,leftremove,rightremove-1,path)
                
            path += char 
            
            if char != "(" and char != ")":
                dfs(index+1,leftcount,rightcount,leftremove,rightremove,path)
            elif char == "(":
                dfs(index+1,leftcount+1,rightcount,leftremove,rightremove,path)
            elif rightcount < leftcount:
                dfs(index+1,leftcount,rightcount+1,leftremove,rightremove,path)
                
            path = path[:len(path)-1]
        
        path = ''
        dfs(0,0,0,l,r,path)
        
        return valid 
        
# @lc code=end

