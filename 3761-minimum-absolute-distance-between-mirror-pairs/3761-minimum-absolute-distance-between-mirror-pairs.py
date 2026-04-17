class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        min_dist = float('inf')
        
        for j, num in enumerate(nums):
            if num in seen:
                min_dist = min(min_dist, j - seen[num])
                
            rev = int(str(num)[::-1])
            seen[rev] = j
        return min_dist if min_dist != float('inf') else -1