from collections import defaultdict

class Solution:
    def distance(self, nums):
        groups = defaultdict(list)
        
        for i, v in enumerate(nums):
            groups[v].append(i)
        
        n = len(nums)
        res = [0] * n
        
        for indices in groups.values():
            prefix = [0]
            
            for x in indices:
                prefix.append(prefix[-1] + x)
            
            m = len(indices)
            
            for i in range(m):
                idx = indices[i]                
                left = i * idx - prefix[i]                
                right = (prefix[m] - prefix[i+1]) - (m - i - 1) * idx
                res[idx] = left + right
        return res