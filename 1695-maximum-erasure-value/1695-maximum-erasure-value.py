class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        max_score = 0
        curr_score = 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_score -= nums[left]
                left += 1

            seen.add(nums[right])
            curr_score += nums[right]
            max_score = max(max_score, curr_score)


        return max_score
        