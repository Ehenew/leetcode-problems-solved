class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n + 1))

        start = 0
        
        while len(players) > 1:
            index = (start + k - 1) % len(players)   
            players.pop(index)
            start = index
        return players[0]
            
        