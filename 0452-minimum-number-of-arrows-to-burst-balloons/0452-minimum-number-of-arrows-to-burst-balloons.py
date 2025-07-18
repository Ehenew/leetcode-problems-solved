class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        count = 1
        curr_arrow = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > curr_arrow:
                count += 1
                curr_arrow = points[i][1]
            else:
                curr_arrow = min(curr_arrow, points[i][1])

        return count 

