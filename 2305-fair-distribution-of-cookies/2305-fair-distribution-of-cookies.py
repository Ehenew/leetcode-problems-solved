class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        distribution_bag = [0] * k

        def dfs(i, distribution_bag):
            if i == n:
                return max(distribution_bag)

            min_unfairness = float('inf')

            for child in range(k):
                distribution_bag[child] += cookies[i]
                min_unfairness = min(min_unfairness, dfs(i+1, distribution_bag))
                distribution_bag[child] -= cookies[i]

                if distribution_bag[child] == 0:
                    break

            return min_unfairness


        return dfs(0, distribution_bag)