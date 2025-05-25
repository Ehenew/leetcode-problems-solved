class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        

        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        
        diff = (aliceSum - bobSum) // 2

        setBob = set(bobSizes)

        for a in aliceSizes:
            b = a - diff
            if b in setBob:
                return [a, b]


