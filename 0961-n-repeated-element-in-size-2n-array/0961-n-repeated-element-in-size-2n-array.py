class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num in freq:
            if freq[num] == len(nums) / 2:
                return num
        return None
        