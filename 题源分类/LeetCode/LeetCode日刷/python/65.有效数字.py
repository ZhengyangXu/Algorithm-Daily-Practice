#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#
# https://leetcode-cn.com/problems/valid-number/description/
#
# algorithms
# Hard (21.28%)
# Likes:    165
# Dislikes: 0
# Total Accepted:    21.4K
# Total Submissions: 100.5K
# Testcase Example:  '"0"'
#
# 验证给定的字符串是否可以解释为十进制数字。
#
# 例如:
#
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
#
# 说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：
#
#
# 数字 0-9
# 指数 - "e"
# 正/负号 - "+"/"-"
# 小数点 - "."
#
#
# 当然，在输入中，这些字符的上下文也很重要。
#
# 更新于 2015-02-10:
# C++函数的形式已经更新了。如果你仍然看见你的函数接收 const char * 类型的参数，请点击重载按钮重置你的代码。
#
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        states = [{},{"blank":1,"sign":2,"digit":3,"dot":4},
                  {"digit":3,"dot":4},
                  {"digit":3,"dot":5,"e|E":6,"blank":9},
                  {"digit":5},
                  {"digit":5,"e|E":6,"blank":9},
                  {"sign":7,"digit":8},
                  {"digit":8},
                  {"digit":8,"blank":9},
                  {"blank":9}
                  ]
        def toChar(s):
            if s == " ":
                return "blank"
            if s == "+" or s == "-":
                return "sign"
            if s.isdigit():
                return "digit"
            if s == ".":
                return "dot"
            if s == "e" or s == "E":
                return "e|E"
            return None 
        
        cur = 1 
        for c in s:
            char = toChar(c)
            if char not in states[cur]:
                return False 
            cur = states[cur][char]
            
        return cur in [3,5,8,9]


# @lc code=end

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        numbers = [str(i) for i in range(10)]
        n = len(s)

        e_show_up, dot_show_up, num_show_up, num_after_e = False, False, False, False

        for i in range(n):
            c = s[i]
            if c in numbers:
                num_show_up = True
                num_after_e = True
            elif c in ('+', '-'):
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif c == '.':
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            elif c == 'e':
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False
            else:
                return False

        return num_show_up