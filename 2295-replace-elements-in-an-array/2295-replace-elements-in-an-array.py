class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos = {num: i for i, num in enumerate(nums)}
        
        for a, b in operations:
            idx = pos[a]          
            nums[idx] = b      
            pos[b] = idx      
        
        return nums
