#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#
# https://leetcode-cn.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (51.99%)
# Likes:    108
# Dislikes: 0
# Total Accepted:    14.3K
# Total Submissions: 27.6K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 
# 如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
# 
# 我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
# 
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 
# 输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 二叉树的节点数介于 2 到 100 之间。
# 每个节点的值都是唯一的、范围为 1 到 100 的整数。
# 
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool: ## 深度优先遍历 + 递归
        if not root:
            return False
        parent ={}
        depth = {}
        def dfs(node,par):
            if node:
                depth[node.val] = 1 + depth[par] if par else 0 
                parent[node.val] = par 
                dfs(node.left,node.val)
                dfs(node.right,node.val)
        dfs(root,None)
        return depth[x] == depth[y] and parent[x] != parent[y]
 
        
# @lc code=end

## 思路：层序遍历。一定要记住层序遍历for循环这个操作，总是忘记，总是死记入栈pop这种操作
## 就加了一个parent的flag进行判断，肯定不是最好的方法。
    # def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    #     if not root:
    #         return False 
        
    #     cur = [(root,root.val)]
        
    #     while cur:
    #         next = []
    #         temp = {}
    #         for node in cur:
    #             cur,parent = node
    #             if cur.left:
    #                 next.append((cur.left,cur.val))
    #             if cur.right:
    #                 next.append((cur.right,cur.val))
                    
    #             temp[cur.val] = parent 
            
    #         if x in temp and y in temp and temp[x] != temp[y]:
    #             return True 
    #         cur = next 
    #     return False 
    
    
        # def isCousins(self, root: TreeNode, x: int, y: int) -> bool: ## 深度优先遍历 + 递归
        # if not root:
        #     return False 
        # dic= {}
        # def dfs(root,depth,parent,target):
        #     if not root:
        #         return
            
        #     if root.val == target:
        #         dic[target] = (depth,parent)
                
            
        #     dfs(root.left,depth+1,root.val,target)
        #     dfs(root.right,depth+1,root.val,target)
            
            
        
        
        # dfs(root,0,0,x)
        # dfs(root,0,0,y)
        # if len(dic) != 2:
        #     return False 
        
        # lis = list(dic.values())
        # if lis[0][0] == lis[1][0] and lis[0][1] != lis[1][1]:
        #     return True