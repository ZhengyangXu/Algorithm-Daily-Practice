#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (57.33%)
# Likes:    943
# Dislikes: 0
# Total Accepted:    184.7K
# Total Submissions: 321.7K
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# 编写一个程序，找到两个单链表相交的起始节点。
#
# 如下面的两个链表：
#
#
#
# 在节点 c1 开始相交。
#
#
#
# 示例 1：
#
#
#
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2,
# skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为
# [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#
#
#
#
# 示例 2：
#
#
#
# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
# 1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为
# [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#
#
#
#
# 示例 3：
#
#
#
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为
# 0，而 skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
#
#
#
#
# 注意：
#
#
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return

        visited = set()
        a,b = headA,headB
        while a:
            if a not in visited:
                visited.add(a)
            a = a.next

        while b:
            if b in visited:
                return b
            b = b.next

        return None





# @lc code=end

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        node1,node2 = headA,headB

        while node1 != node2:
            if node1:
                node1 = node1.next
            else:
                node1 = headB
            if node2:
                node2 = node2.next
            else:
                node2 = headA
        return node1

    def getIntersectionNode(self, headA: ListNode,headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        node1, node2 = headA, headB
        stack1, stack2 = [], []
        while node1:
            stack1.append(node1)
            node1 = node1.next

        while node2:
            stack2.append(node2)
            node2 = node2.next

        res = None
        while stack1 and stack2:
            p1, p2 = stack1.pop(), stack2.pop()
            if p1.val == p2.val:
                res = p1
                continue
            if not stack1 or not stack2:
                return None
        return res

    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        if not headA or not headB:
            return

        visited = set()
        a, b = headA, headB
        while a:
            if a not in visited:
                visited.add(a)
            a = a.next

        while b:
            if b in visited:
                return b
            b = b.next

        return None
