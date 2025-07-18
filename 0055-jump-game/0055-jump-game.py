class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0

        for i in range(len(nums)):         
            if i > max_pos:
                return False
            max_pos = max(max_pos, i + nums[i])

          
        return True

        