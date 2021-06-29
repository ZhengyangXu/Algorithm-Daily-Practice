#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#
# https://leetcode-cn.com/problems/bus-routes/description/
#
# algorithms
# Hard (33.77%)
# Likes:    185
# Dislikes: 0
# Total Accepted:    17.5K
# Total Submissions: 43.4K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
#
#
# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1
# -> ... 这样的车站路线行驶。
#
#
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
#
# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
#
#
#
# 示例 1：
#
#
# 输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。
#
#
# 示例 2：
#
#
# 输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1 .
# 1
# routes[i] 中的所有值 互不相同
# sum(routes[i].length)
# 0
# 0
#
#
#

# @lc code=start
class Solution:

    def numBusesToDestination(self, routes: List[List[int]], source: int,
                              target: int) -> int:
        if source == target:
            return 0
        
        stations = defaultdict(set)
        
        for i,route in enumerate(routes):
            for stop in route: 
                stations[stop].add(i) 
        routes = [set(x) for x in routes]
        
        buses = set()
        stops = {source}
        front = {source}
        back = {target}
        cost = 0
        
        while front and back:
            nexstops = set() 
            
            for curstop in front:
                for curbus in stations[curstop] - buses:
                    for targetstop in back:
                        if curbus in stations[targetstop]:
                            return cost + 1 
                    buses.add(curbus)
                    
                    for nexstop in routes[curbus] - stops:
                        stops.add(nexstop)
                        nexstops.add(nexstop)
            front = back 
            back = nexstops 
            cost += 1 
        return -1 
                
                    





# @lc code=end

    def numBusesToDestination(self, routes: List[List[int]], source: int,
                              target: int) -> int:
        if source == target:
            return 0

        stations = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stations[stop].add(i)

        routes = [set(route) for route in routes]

        buses = set()
        q = [(source, 0)]

        stops = {source}

        while q:

            cur, cost = q.pop(0)

            if cur == target:
                return cost

            for bus in stations[cur] - buses:
                for stop in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(stop)
                    q.append((stop, cost + 1))
        return -1