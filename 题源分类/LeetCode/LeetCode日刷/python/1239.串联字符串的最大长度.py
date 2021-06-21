#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#
# https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#
# algorithms
# Medium (41.31%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    31.8K
# Total Submissions: 65K
# Testcase Example:  '["un","iq","ue"]'
#
# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
#
# 请返回所有可行解 s 中最长长度。
#
#
#
# 示例 1：
#
# 输入：arr = ["un","iq","ue"]
# 输出：4
# 解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
#
#
# 示例 2：
#
# 输入：arr = ["cha","r","act","ers"]
# 输出：6
# 解释：可能的解答有 "chaers" 和 "acters"。
#
#
# 示例 3：
#
# 输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
# 输出：26
#
#
#
#
# 提示：
#
#
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] 中只含有小写英文字母
#
#
#


# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int: ##常规回溯
        
        new_arr = [s for s in arr if len(s) == len(set(s))]
        ans = 0
        def backtrack(new_arr,path):
            nonlocal ans 
            if len(new_arr) == 0 :
                print("最终path:{}".format(path))
                ans = max(ans,len(''.join(path)))
                return 
                
            for i in range(len(new_arr)):
                print("初始path:{}".format(path))
                flag = True 
                if path:
                    print("判断path:{},arr[i]:{}".format(path,new_arr[i]))
                    for ch in path:
                        for ch2 in new_arr[i]:
                            if ch2 in ch:
                                flag = False   
                        else:
                            continue 
                        break 
                if flag:
                    path.append(new_arr[i])
                    print("path append:{}".format(path))
                    backtrack(new_arr[i+1:],path)
                    print("path continue:{}".format(path))
                    path.pop() 
                    print("path pop:{}".format(path))
        backtrack(new_arr,[])
        return ans 
                
 


# @lc code=end

    def maxLength(self, arr: List[str]) -> int:
        masks = list()
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord('a')
                if (mask >> idx) & 1:
                    mask = 0
                    break
                mask |= 1 << idx
            if mask > 0:
                masks.append(mask)
        ans = 0

        def backtrack(pos, mask):
            nonlocal ans
            if pos == len(masks):
                ans = max(ans, bin(mask).count("1"))
                return

            if (mask & masks[pos]) == 0:
                backtrack(pos + 1, mask | masks[pos])
            backtrack(pos + 1, mask)

        backtrack(0, 0)

        return ans
    
    
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        masks = [0]

        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord('a')
                if (mask >> idx) & 1:
                    mask = 0
                    break
                mask |= 1 << idx
            if mask == 0:
                continue

            n = len(masks)
            for i in range(n):
                m = masks[i]
                if m & mask == 0:
                    masks.append(m | mask)
                    ans = max(ans, bin(masks[-1]).count("1"))
        return ans
