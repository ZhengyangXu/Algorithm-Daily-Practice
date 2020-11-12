#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (51.06%)
# Likes:    986
# Dislikes: 0
# Total Accepted:    110.6K
# Total Submissions: 216.6K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
# 
# 
# 
# 实现 LRUCache 类：
# 
# 
# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value)
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
# 
# 
# 
# 
# 
# 
# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 0 
# 最多调用 3 * 10^4 次 get 和 put
# 
# 
#

# @lc code=start

      
class Node:
  def __init__(self,key,val):
    self.val = val
    self.key = key
    self.next = None
    self.prev = None 

class DoubleList:
  
  def __init__(self):
    self.head = Node(0,0)
    self.tail = Node(0,0)
    self.head.next = self.tail  
    self.tail.prev = self.head
    self.size = 0 
    
  def addFirst(self,node):
    node.next = self.head.next  
    node.prev = self.head   
    self.head.next.prev = node  
    self.head.next = node  
    self.size += 1 
    
  def remove(self,node):
    node.prev.next = node.next  
    node.next.prev = node.prev 
    self.size -= 1
    
  def removeLast(self):
    if self.tail.prev == self.head:
      return None  
    
    last = self.tail.prev
    self.remove(last)
    return last

class LRUCache:
  
    def __init__(self, capacity: int):
      self.cap = capacity   
      self.map = dict()
      self.cache = DoubleList()
      
      


    def get(self, key: int) -> int:
      if key not in self.map:
        return -1 
      else:
        node = self.map[key]
        self.cache.remove(node)
        self.cache.addFirst(node)
        return node.val 


    def put(self, key: int, value: int) -> None:
      
      node = Node(key,value)
      if key in self.map:
        self.cache.remove(node)
        self.cache.addFirst(node)
        self.map[key] = node  
      else:
        if self.cap < self.cache.size:
          last = self.cache.removeLast() 
          self.map.pop(last.key)
      self.cache.addFirst(node)
      self.map[key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

# class Node:
#   def __init__(self,val,key):
#     self.val = val
#     self.key = key
#     self.next = None
#     self.prev = None 

# class DoubleList:
  
#   def __init__(self):
#     self.head = Node(0,0)
#     self.tail = Node(0,0)
#     self.head.next = self.tail  
#     self.tail.prev = self.head
#     self.size = 0 
    
#   def addFirst(self,x):
#     x.next = self.head.next  
#     x.prev = self.head   
#     self.head.next.prev = x  
#     self.head.next = x  
#     self.size += 1 
    
#   def remove(self,x):
#     x.prev.next = x.next  
#     x.next.prev = x.prev 
#     self.size -= 1
    
#   def removeLast(self):
#     if self.tail.prev == self.head:
#       return None  
    
#     last = self.tail.prev
#     self.remove(last)
#     return last

# class LRUCache:
  
#     def __init__(self, capacity: int):
#       self.cap = capacity   
#       self.map = dict()
#       self.cache = DoubleList()
      
      


#     def get(self, key: int) -> int:
#       if key not in self.map:
#         return -1 
#       else:
#         val = self.map[key].val  
#         self.put(key,val)
#         return val  


#     def put(self, key: int, value: int) -> None:
      
#       x = Node(key,value)
#       if key in self.map:
#         self.cache.remove(self.map[key])
#         self.cache.addFirst(x)
#         self.map[key] = x  
#       else:
#         if self.cap == self.cache.size:
#           last = self.cache.removeLast() 
#           self.map.pop(last.key)
#       self.cache.addFirst(x)
#       self.map[key] = x 

# class DLinkedNode:
#     def __init__(self, key=0, value=0):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = dict()
#         # 使用伪头部和伪尾部节点    
#         self.head = DLinkedNode()
#         self.tail = DLinkedNode()
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.capacity = capacity
#         self.size = 0

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         # 如果 key 存在，先通过哈希表定位，再移到头部
#         node = self.cache[key]
#         self.moveToHead(node)
#         return node.value

#     def put(self, key: int, value: int) -> None:
#         if key not in self.cache:
#             # 如果 key 不存在，创建一个新的节点
#             node = DLinkedNode(key, value)
#             # 添加进哈希表
#             self.cache[key] = node
#             # 添加至双向链表的头部
#             self.addToHead(node)
#             self.size += 1
#             if self.size > self.capacity:
#                 # 如果超出容量，删除双向链表的尾部节点
#                 removed = self.removeTail()
#                 # 删除哈希表中对应的项
#                 self.cache.pop(removed.key)
#                 self.size -= 1
#         else:
#             # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
#             node = self.cache[key]
#             node.value = value
#             self.moveToHead(node)
    
#     def addToHead(self, node):
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node
    
#     def removeNode(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev

#     def moveToHead(self, node):
#         self.removeNode(node)
#         self.addToHead(node)

#     def removeTail(self):
#         node = self.tail.prev
#         self.removeNode(node)
#         return node
            