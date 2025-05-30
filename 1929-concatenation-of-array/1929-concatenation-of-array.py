class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        right_half = []

        for i in range(len(nums)):
            right_half.append(nums[i])
        return nums + right_half