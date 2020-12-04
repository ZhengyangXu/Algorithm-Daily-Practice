#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (45.45%)
# Likes:    655
# Dislikes: 0
# Total Accepted:    89.4K
# Total Submissions: 196.7K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
# 
#

# @lc code=start
class Solution:
    from collections import defaultdict
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int: #双端DFS
        
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0 
        
        wordset = set(wordList)
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)
        
        begin_visited = set()
        begin_visited.add(beginWord)
        end_visited = set()
        end_visited.add(endWord)
        
        step = 1 
        
        while begin_visited and end_visited:
            
            next_level = set()
            
            if len(begin_visited) > len(end_visited):
                begin_visited,end_visited = end_visited,begin_visited 
                
            for word in begin_visited:
                word_list = list(word)
                
                for i in range(len(word_list)):
                    ochar = word_list[i]  
                    for k in range(26):
                        word_list[i] = chr(ord("a")+k)
                        cur_word = "".join(word_list)
                        
                        if cur_word in wordset:
                            if cur_word in end_visited:
                                return step+1 
                            if cur_word not in visited:
                                visited.add(cur_word)
                                next_level.add(cur_word)
                    word_list[i] = ochar 
            begin_visited = next_level 
            step += 1 
        return 0 
                


  
                     
                

        
        

        
# @lc code=end
        # word_set = set(wordList)
        # if len(word_set) == 0 or endWord not in word_set:
        #     return 0 
        
        # if beginWord in word_set:
        #     word_set.remove(beginWord)
            
        # queue = []
        # queue.append(beginWord)
        
        # visited=set(beginWord)
        # word_len = len(beginWord)
        
        # step = 1 
        
        # while queue:
        #     current_size = len(queue)
        #     for i in range(current_size):
        #         word = queue.pop(0)
        #         word_list = list(word)
        #         for j in range(word_len):
        #             ochar = word_list[j]
                    
        #             for k in range(26):
        #                 word_list[j] = chr(ord('a')+k)
        #                 next_word = ''.join(word_list)
        #                 if next_word in word_set:
        #                     if next_word == endWord:
        #                         return step+1 
        #                     if next_word not in visited:
        #                         queue.append(next_word)
        #                         visited.add(next_word)
        #             word_list[j] = ochar
        #     step += 1 
        
        # return 0
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int: BFS
        
    #     if not beginWord or not endWord or not wordList or endWord not in wordList:
    #         return 0 
        
    #     wordset = set(wordList)
    #     if beginWord in wordset:
    #         wordset.remove(beginWord)
    #     queue = [beginWord]
    #     visited = set(beginWord)
    #     wordlen = len(beginWord)
    #     step = 1
        
    #     while queue:
    #         for _ in range(len(queue)):
    #             cur_word = list(queue.pop(0))
    #             for i in range(wordlen):
    #                 ochar = cur_word[i]
    #                 for letter in range(26):
    #                     cur_word[i] = chr(ord("a")+letter)
    #                     next_word = "".join(cur_word)
    #                     if next_word in wordset:
    #                         if next_word == endWord:
    #                             return step+1  
    #                         if next_word not in visited:
    #                             visited.add(next_word)
    #                             queue.append(next_word)
    #                 cur_word[i] = ochar 
    #         step += 1
    #     return 0     
    
    
    
    #  from collections import defaultdict 常规BFS 超时
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
    #     if not beginWord or not endWord or not wordList:
    #         return False 
        
    #     def isValid(word1,word2):
    #         count = 0 
    #         if len(word1) != len(word2):
    #             return False  
    #         for i in range(len(word1)):
    #             if word1[i] != word2[i]:
    #                 count += 1 
    #         if count != 1:
    #             return False 
    #         return True 
        
    #     graph = defaultdict(list)
    #     wordset = set(wordList)
    #     if beginWord not in wordset:
    #         wordset.add(beginWord)
    #     for word1 in wordset:
    #         for word2 in wordset:
    #             if word1 != word2 and isValid(word1,word2):
    #                 graph[word1].append(word2) 
                    

    #     visited = set(beginWord)
    #     queue = [(beginWord,1)]
    #     while queue:
    #         cur_word,step = queue.pop(0) 
    #         next_word = graph[cur_word]
    #         for next in next_word:
    #             if next == endWord:
    #                 return step+1
    #             if next not in visited:
    #                 visited.add(next)
    #                 queue.append((next,step+1))
            
    #     return 0 
