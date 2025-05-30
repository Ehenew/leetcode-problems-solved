class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        my_dict = {}
        pairs_count = 0

        for num in nums:
            my_dict[num] = my_dict.get(num , 0) + 1
            if my_dict[num] == 2:
                pairs_count += 1
                del my_dict[num]
            
        leftover_count = len(my_dict)

        return [pairs_count, leftover_count]
