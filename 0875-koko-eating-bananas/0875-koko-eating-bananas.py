class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            tot_time = sum(math.ceil(pile / k) for pile in piles)

            if tot_time <= h:
                res = k
                right = k - 1   
            else:
                left = k + 1   

        return res
