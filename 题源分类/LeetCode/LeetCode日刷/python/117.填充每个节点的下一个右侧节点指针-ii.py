#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (59.42%)
# Likes:    362
# Dislikes: 0
# Total Accepted:    63.1K
# Total Submissions: 106.2K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# 给定一个二叉树
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 
# 初始状态下，所有 next 指针都被设置为 NULL。
# 
# 
# 
# 进阶：
# 
# 
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数小于 6000
# -100 <= node.val <= 100
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def getNext(root):
            while root.next:
                if root.next.left:
                    return root.next.left 
                if root.next.right:
                    return root.next.right  
                
                root = root.next  
            return 
        
        if not root or not root.left and not root.right:
            return root
        
        if root.left and root.right:
            root.left.next = root.right  
            root.right.next = getNext(root)
        
        if not root.left:
            root.right.next = getNext(root)
            
        if not root.right:
            root.left.next = getNext(root)
            
        root.right = self.connect(root.right)
        root.left = self.connect(root.left)
        
        
        return root 
# @lc code=end

    # def connect(self, root: 'Node') -> 'Node':
        
    #     if not root:
    #         return
        
    #     cur = [root]
        
    #     while cur: 
    #         nex = []
            
    #         for i in range(len(cur)): 
    #             node = cur[i]
    #             node.next = cur[i+1] if i < len(cur)-1 else None
    #             if node.left:
    #                 nex.append(node.left)
    #             if node.right:
    #                 nex.append(node.right)
                    
    #         cur = nex
        
    #     return root
    
    
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root:
    #         return 
        
    #     cur = root 
    #     while cur:
    #         dummy = Node()
    #         tail = dummy  
    #         while cur:
    #             if cur.left:
    #                 tail.next = cur.left 
    #                 tail = tail.next 
    #             if cur.right:
    #                 tail.next = cur.right 
    #                 tail = tail.next  
    #             cur = cur.next 
    #         cur = dummy.next 
    #     return root