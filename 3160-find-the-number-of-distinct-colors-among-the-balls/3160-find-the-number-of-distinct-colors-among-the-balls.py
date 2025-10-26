from collections import Counter

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        ball_to_color = {}            
        c_count = Counter()       
        
        res = []
        for ball, color in queries:
            if ball in ball_to_color:
                old = ball_to_color[ball]
                c_count[old] -= 1
                if c_count[old] == 0:
                    del c_count[old]
            
            ball_to_color[ball] = color
            c_count[color] += 1            
            res.append(len(c_count))
        
        return res
