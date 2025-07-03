from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()

        while queue:
            room = queue.popleft()
            if room in visited:
                continue
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
            
        return len(visited) == len(rooms)





