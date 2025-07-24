class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # print(intervals)

        count = 0
        init_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < init_end:
                count +=  1
            else:
                init_end = end
        
        return count