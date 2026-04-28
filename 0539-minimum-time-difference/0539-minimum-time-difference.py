class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        
        for t in timePoints:
            h, m = map(int, t.split(":"))
            minutes.append(h * 60 + m)        
        minutes.sort()  
              
        ans = float('inf')
        
        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])
        
        ans = min(ans, minutes[0] + 1440 - minutes[-1])
        return ans