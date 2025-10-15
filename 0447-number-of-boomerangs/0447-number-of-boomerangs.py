class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in points:
            dist_count = {}
            for j in points:
                if i == j:
                    continue
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                dist = dx * dx + dy * dy
                dist_count[dist] = dist_count.get(dist, 0) + 1
            for count in dist_count.values():
                res += count * (count - 1)
        return res

        