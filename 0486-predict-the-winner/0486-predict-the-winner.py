class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def score(start, end):
            if start == end:
                return nums[start]
            choose_start = nums[start] - score(start + 1, end)
            choose_end = nums[end] - score(start, end - 1)
            return max(choose_start, choose_end)

        return score(0, len(nums) - 1) >= 0
