class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:        
        ops = 0

        while target > 1:
            if maxDoubles == 0:
                ops += target - 1
                break
            elif maxDoubles > 0  and target % 2 == 0:
                target = target // 2
                maxDoubles -= 1
                ops += 1
            else:
                target -= 1
                ops += 1

        return ops
            



        