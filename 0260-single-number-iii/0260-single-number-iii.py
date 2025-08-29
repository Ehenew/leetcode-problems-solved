class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xored = 0
        for num in nums:
            xored ^= num

        mask =  xored & (~xored + 1) 
        n1 = 0
        n2 = 0
        for num in nums:
            if num & mask:   
                n1 ^= num
            else:           
                n2 ^= num

        return [n1, n2] 