class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Step 1: Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize the merged intervals list with the first interval
        merged = [intervals[0]]
        
        # Step 3: Iterate through the rest of the intervals
        for current in intervals[1:]:
            # Compare current interval with the last merged interval
            last_merged = merged[-1]
            
            # If there is an overlap, merge the intervals
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add the current interval as a new merged interval
                merged.append(current)
        
        return merged
