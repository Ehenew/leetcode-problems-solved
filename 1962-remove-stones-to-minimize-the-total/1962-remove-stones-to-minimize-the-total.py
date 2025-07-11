class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        

        for _ in range(k):
            piles.sort()

            piles[-1] = math.ceil(piles[-1] / 2)

        return sum(piles)
    
            