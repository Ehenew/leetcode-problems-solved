class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        radius = 0
        
        for house in houses:            
            left, right = 0, len(heaters) - 1
            #  houses = [1,2,3,4],
            #  heaters = [1,4]

            while left < right:
                mid = (left + right) // 2

                if heaters[mid] <= house:
                    left = mid + 1
                else:
                    right = mid
            dist = abs(heaters[left] - house )

            if left > 0:
                dist = min(dist, abs(heaters[left - 1 ] - house))
            radius = max(radius, dist)                
        return radius