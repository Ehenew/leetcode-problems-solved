class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # in_degree[judge] = n - 1
        # out_degree[judge] = 0

        trust_value = [0] * (n + 1)


        for a, b in trust:
            trust_value[a] -= 1
            trust_value[b] += 1

        for i in range(1, n + 1):
            if trust_value[i] == n -1:
                return i
        return -1