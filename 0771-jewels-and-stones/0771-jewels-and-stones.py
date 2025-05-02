class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_jewels = 0
        for stone in stones:
            if stone in jewels:
                count_jewels += 1
        return count_jewels