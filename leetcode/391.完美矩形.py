#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#
# https://leetcode-cn.com/problems/perfect-rectangle/description/
#
# algorithms
# Hard (28.94%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 7.6K
# Testcase Example:  '[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]'
#
# 我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。
# 
# 每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 ( 左下角的点的坐标为 (1, 1)
# 以及右上角的点的坐标为 (2, 2) )。
# 
# 
# 
# 示例 1:
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4],
# ⁠ [1,3,2,4],
# ⁠ [2,3,3,4]
# ]
# 
# 返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
# 
# 
# 
# 
# 
# 
# 示例 2:
# 
# rectangles = [
# ⁠ [1,1,2,3],
# ⁠ [1,3,2,4],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4]
# ]
# 
# 返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
# 
# 
# 
# 
# 
# 
# 示例 3:
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [3,2,4,4]
# ]
# 
# 返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
# 
# 
# 
# 
# 
# 
# 示例 4:
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [2,2,4,4]
# ]
# 
# 返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
# 
# 
#

# @lc code=start
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        actual_area = 0 
        
        X1,Y1,X2,Y2 = float('inf'),float('inf'),-float('inf'),-float('inf')
        points = set()
        for x1,y1,x2,y2 in rectangles:
            X1,Y1 = min(X1,x1),min(Y1,y1)
            X2,Y2 = max(X2,x2),max(Y2,y2)
            
            actual_area += (y2-y1) * (x2-x1)
            for p in [(x1,y1),(x2,y2),(x1,y2),(x2,y1)]:
                if p not in points:
                    points.add(p)
                else:
                    points.remove(p)
        
        perfect_area = (Y2-Y1) * (X2 - X1)
        if perfect_area != actual_area:
            return False 
        
        if len(points) != 4:
            return False  
        
        for point in points:
            if point not in [(X1,Y1),(X2,Y2),(X1,Y2),(X2,Y1)]:
                return False   
        
        return True 
        
        
# @lc code=end

## 思路：完美矩形的面积和小矩形面积之和相等，且小矩形合起来之后的顶点只有4个才可行程完美矩形。
