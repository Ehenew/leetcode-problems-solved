class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums_array = []
        
        for i in range(len(nums)):
            nums_array.append(nums[nums[i]])

        return nums_array
