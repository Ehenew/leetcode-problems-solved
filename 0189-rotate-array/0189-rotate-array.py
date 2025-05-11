class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            last = nums[-1]
            for i in range(len(nums) -1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = last
        