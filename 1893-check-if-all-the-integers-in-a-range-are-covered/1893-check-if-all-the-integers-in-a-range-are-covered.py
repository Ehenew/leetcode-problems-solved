class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for num in range(left, right + 1):
            found = False
            for arr in ranges:
                if arr[0] <= num <= arr[1]:
                    found = True
                    break
            if not found:
                return False
        return True
            