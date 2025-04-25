class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # Step 1: Add all intervals before the new interval that do not overlap
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Step 2: Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])  # Update start time
            newInterval[1] = max(newInterval[1], intervals[i][1])  # Update end time
            i += 1
        
        # Add the merged interval to the result
        result.append(newInterval)
        
        # Step 3: Add all remaining intervals after the new interval
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
