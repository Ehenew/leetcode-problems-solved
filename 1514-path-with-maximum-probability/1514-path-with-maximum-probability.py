import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        heap = [(-1.0, start_node)]
        probs = [0.0] * n
        probs[start_node] = 1.0
        
        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob              
            if node == end_node:
                return prob
            
            for nei, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > probs[nei]:
                    probs[nei] = new_prob
                    heapq.heappush(heap, (-new_prob, nei))
        
        return 0.0
