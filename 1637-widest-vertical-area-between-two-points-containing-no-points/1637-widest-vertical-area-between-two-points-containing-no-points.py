class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        max_width = 0

        for i in range(1,n):
            width = points[i][0] - points[i-1][0]
            max_width = max(max_width, width) 

        return max_width