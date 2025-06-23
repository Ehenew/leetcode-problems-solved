class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Step 1: Store (start, original_index)
        start_index_pairs =[]
        
        for i, interval in enumerate(intervals):
            start_index_pairs.append((interval[0], i)) 


        start_index_pairs.sort()

        result = []

        for interval in intervals:
            end = interval[1]
            
            left, right = 0, n - 1
            idx = -1  

            while left <= right:
                mid = (left + right) // 2
                if start_index_pairs[mid][0] >= end:
                    idx = start_index_pairs[mid][1] 
                    right = mid - 1  
                else:
                    left = mid + 1

            result.append(idx)

        return result

            