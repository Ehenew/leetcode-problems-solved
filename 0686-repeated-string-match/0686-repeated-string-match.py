import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not set(b).issubset(set(a)):
            return -1

        n, m = len(a), len(b)
        min_reps = math.ceil(m / n)

        s = a * min_reps
        if b in s:
            return min_reps
        s += a
        if b in s:
            return min_reps + 1

        return -1