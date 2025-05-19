class Solution:
    def triangleType(self, nums: List[int]) -> str:
        try_type = ''

        if nums[0] + nums[1] <= nums[2] or nums[0] + nums[2] <= nums[1] or nums[1] + nums[2] <= nums[0]:
            return 'none'
        if nums[0] == nums[1] == nums[2]:
            tri_type = "equilateral"
        elif nums[0] != nums[1] and nums[1]!= nums[2] and nums[0]!= nums[2] :
            tri_type = 'scalene'
        else:
            tri_type = 'isosceles'
        
        return tri_type