class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(path, curr_num):
            if len(path) == k:
                res.append(path[:])
                return 
            
            for i in range(curr_num, n + 1):
                path.append(i) 
                backtrack(path, i + 1)
                path.pop()

    
        res = []
        backtrack([], 1)
        return res
