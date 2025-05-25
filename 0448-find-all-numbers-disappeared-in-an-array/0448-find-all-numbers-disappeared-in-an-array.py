class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        expected_numbers = set(range(1, len(nums) + 1))
        current_numbers = set(nums)
        return list(expected_numbers - current_numbers)
