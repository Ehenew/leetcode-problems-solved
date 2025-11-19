class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        for a, b in allowedSwaps:
            union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(i)

        hamming = 0
        for comp in groups.values():
            count_source = Counter(source[i] for i in comp)
            count_target = Counter(target[i] for i in comp)
            for val, freq in count_source.items():
                extra = freq - count_target.get(val, 0)
                if extra > 0:
                    hamming += extra
        return hamming