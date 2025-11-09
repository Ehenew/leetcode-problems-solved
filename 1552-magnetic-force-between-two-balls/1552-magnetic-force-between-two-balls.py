class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        
        def canPlace(distance):
            count = 1
            last = position[0]
            for pos in position[1:]:
                if pos - last >= distance:
                    count += 1
                    last = pos
                    if count == m:
                        return True
            return False
        
        left, right = 1, position[-1] - position[0]
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canPlace(mid):
                best = mid
                left = mid + 1 
            else:
                right = mid - 1         
        return best