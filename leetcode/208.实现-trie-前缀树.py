#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (69.08%)
# Likes:    470
# Dislikes: 0
# Total Accepted:    62.7K
# Total Submissions: 90.6K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
# 
# 示例:
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true
# 
# 说明:
# 
# 
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。
# 
# 
#

# @lc code=start
class Trie:
    
    class Node:
        def __init__(self):
            self.is_word = False 
            self.dict = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.Node()
  


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root 
        for alpha in word:
            if alpha not in cur_node.dict:
                cur_node.dict[alpha] = Trie.Node() 
            
            cur_node = cur_node.dict[alpha]
        
        if not cur_node.is_word:
            cur_node.is_word = True
            
            


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root 
        for alpha in word:
            if alpha not in cur_node.dict: 
                return False 
            else:
                cur_node = cur_node.dict[alpha]
        
        return cur_node.is_word
    


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root 
        for alpha in prefix:
            if alpha not in cur_node.dict:
                return False 
            else:
                cur_node = cur_node.dict[alpha]
        
        return True 



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

