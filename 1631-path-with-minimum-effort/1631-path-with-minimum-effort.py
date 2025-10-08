import heapq
import math

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        diff = [[float('inf')] * n for _ in range(m)]
        diff[0][0] = 0
        
        heap = [(0, 0, 0)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        while heap:
            effort, i, j = heapq.heappop(heap)
            if i == m - 1 and j == n - 1:
                return effort

            if effort > diff[i][j]:
                continue
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    new_diff = abs(heights[i][j] - heights[x][y])
                    new_effort = max(effort, new_diff)
                    if new_effort < diff[x][y]:
                        diff[x][y] = new_effort
                        heapq.heappush(heap, (new_effort, x, y))
        return 0  