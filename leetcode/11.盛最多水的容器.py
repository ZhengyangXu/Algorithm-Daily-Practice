#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (63.93%)
# Likes:    1777
# Dislikes: 0
# Total Accepted:    271.5K
# Total Submissions: 423.9K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 
# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 
# 
# 
# 
# 
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 
# 
# 
# 示例：
# 
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int: ## 双指针 看的答案 
        l,r = 0,len(height)-1
        ans = 0 
        while l < r:
            area = min(height[l],height[r])*(r-l)
            ans = max(ans,area)
            if height[l] < height[r]:
                l += 1 
            else:
                r -= 1 
        return ans 
# @lc code=end
### 思路：双指针。容水的最大值就是左右两个指针值娇小的内个*指针之间的距离。直觉上每次移动应该移动指针值较小
#的内个，实际上也是这样。假如左边的l较小，min(h[l],h[r)=l,距离=r-l.如果移动右指针，则min(h[l],h[r-1])<=min(h[l],h[r-1])
#因为如果h[r-1]大于h[l],最小值还是h[l],如果h[r-1]小于h[l],那最小值是h[r-1],同时两个指针距离变为r-l-1
#无论如何，移动右指针都不会使得面积更大。











