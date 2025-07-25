class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0
        for i in range(n - 2, -1, -1):
            while nums[i] > nums[i + 1]:
                part1 = math.ceil(nums[i] / 2)
                part2 = nums[i] - part1
                ops += 1
                nums[i] = max(part1, part2)
        return ops
