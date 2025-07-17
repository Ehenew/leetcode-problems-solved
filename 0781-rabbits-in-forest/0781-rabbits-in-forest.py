from collections import defaultdict

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = defaultdict(int)

        for ans in answers:
            freq[ans] += 1
        
        tot_rabbits = 0
        for f in freq:
            group_size = f + 1
            tot_groups = math.ceil(freq[f] / group_size)
            tot_rabbits += tot_groups * group_size
        
        return tot_rabbits