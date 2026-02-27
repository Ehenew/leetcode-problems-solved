class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num
        
        earn2, earn1 = 0, 0
        for v in points:
            earn2, earn1 = earn1, max(earn1, earn2 + v)        
        return earn1