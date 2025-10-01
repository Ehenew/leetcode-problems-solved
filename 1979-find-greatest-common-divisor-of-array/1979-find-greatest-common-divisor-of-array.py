class Solution:
    def findGCD(self, nums: List[int]) -> int:        
        smallest, largest = min(nums), max(nums)
        while smallest:
            largest, smallest = smallest, largest % smallest
        return largest
