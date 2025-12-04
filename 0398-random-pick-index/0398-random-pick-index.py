import random
class Solution:

    def __init__(self, nums: List[int]):
        self.positions = {}
        for i, n in enumerate(nums):
            if n not in self.positions:
                self.positions[n] = []
            self.positions[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.positions[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)