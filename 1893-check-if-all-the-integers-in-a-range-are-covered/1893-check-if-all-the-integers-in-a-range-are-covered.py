class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for num in range(left, right + 1):
            found = False
            for r in ranges:
                if r[0] <= num <= r[1]:
                    found = True
                    break
            if not found:
                return False
        return True
            