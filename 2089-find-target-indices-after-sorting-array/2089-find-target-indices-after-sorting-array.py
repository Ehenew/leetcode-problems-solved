class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []

        for i in range(1, len(nums)):
            min_element = nums[i]
            j = i - 1

            while min_element < nums[j] and j > - 1:
                nums[j + 1] = nums[j]
                nums[j] = min_element
                j -= 1

        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res
