class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()

        curr_target = 1

        for coin in coins:
            if coin <= curr_target:
                curr_target += coin
            else:
                break
        
        return curr_target