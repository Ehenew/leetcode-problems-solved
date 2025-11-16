from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_graph = defaultdict(list)
        item_indegree = [0] * n
        group_graph = defaultdict(list)
        group_indegree = [0] * m

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                if group[prev] != group[curr]:  
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1
        
        def topo_sort(graph, indegree, total):
            q = deque([i for i in range(total) if indegree[i] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return order if len(order) == total else []

        group_order = topo_sort(group_graph, group_indegree, m)
        if not group_order:
            return []

        item_order = topo_sort(item_graph, item_indegree, n)
        if not item_order:
            return []

        group_to_items = defaultdict(list)
        for item in item_order:
            group_to_items[group[item]].append(item)

        result = []
        for g in group_order:
            result.extend(group_to_items[g])

        return result