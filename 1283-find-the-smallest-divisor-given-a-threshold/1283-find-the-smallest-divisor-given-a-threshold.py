class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
       
        left, right = 1, max(nums)
        
        def compute_sum(divisor):
            total = 0
            for num in nums:
                total += math.ceil(num / divisor)
            return total

        
        while left < right:
            mid = (left + right) // 2
            if compute_sum(mid) <= threshold:
                right = mid   
            else:
                left = mid + 1  
        
        return left
