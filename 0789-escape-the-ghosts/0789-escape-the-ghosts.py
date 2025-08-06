class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        def calc_distance(x, y):
            return abs(target[0] - x) + abs(target[1] - y)

        my_distance = calc_distance(0, 0)

        for gx, gy in ghosts:
            if calc_distance(gx, gy) <= my_distance:
                return False

        return True
