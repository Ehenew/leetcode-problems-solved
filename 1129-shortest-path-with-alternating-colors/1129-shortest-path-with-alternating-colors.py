from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph_red = defaultdict(list)
        graph_blue = defaultdict(list)

        for a, b in redEdges:
            graph_red[a].append(b) 
        
        for u, v in blueEdges:
            graph_blue[u].append(v) 


        queue = deque([(0, 'red', 0), (0, 'blue', 0)]) # (node, color, distance)
        ans = [-1] * n
        visited = set({(0, 'red'), (0, 'blue')})

        while queue:
            node, color, distance = queue.popleft()

            if ans[node] == -1:
                ans[node] = distance

            if color == 'red':
                for neighbor in graph_blue[node]: # alternating colors
                    if (neighbor, 'blue') not in visited:
                        visited.add((neighbor, 'blue'))
                        queue.append((neighbor, 'blue', distance + 1))
            else:
                for neighbor in graph_red[node]:
                    if (neighbor, 'red') not in visited:
                        visited.add((neighbor, 'red'))
                        queue.append((neighbor, 'red', distance + 1))
        return ans