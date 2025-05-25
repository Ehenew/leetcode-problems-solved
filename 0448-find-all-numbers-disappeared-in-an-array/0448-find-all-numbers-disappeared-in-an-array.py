class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_numbers = set(range(1, len(nums) + 1))
        present_numbers = set(nums)
        return list(all_numbers - present_numbers)
