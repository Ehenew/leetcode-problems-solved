class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            curr_days = 1
            curr_total = 0

            for weight in weights:
                if weight + curr_total > mid:
                    curr_days += 1
                    curr_total = 0
                curr_total += weight
            
            if  curr_days <= days:
                right = mid
            else:
                left  = mid + 1
            
        return left
                

            



    
