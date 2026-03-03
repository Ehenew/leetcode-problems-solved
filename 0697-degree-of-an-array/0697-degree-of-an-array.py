class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        count = {}
        
        for i, v in enumerate(nums):
            if v not in first:
                first[v] = i
            last[v] = i
            count[v] = count.get(v, 0) + 1
        
        degree = max(count.values())
        
        min_len = float('inf')
        for v in count:
            if count[v] == degree:
                length = last[v] - first[v] + 1
                min_len = min(min_len, length)
        return min_len