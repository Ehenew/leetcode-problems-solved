class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
       
        answer = [0] * len(nums)
        left = 0
        
        for num in nums:
            if num != 0:
               answer[left] = num
               left += 1
        return answer