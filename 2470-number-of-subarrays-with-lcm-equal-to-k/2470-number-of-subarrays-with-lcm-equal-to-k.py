import math
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
            n = len(nums)
            count = 0
            
            for i in range(n):
                cur_lcm = 1
                for j in range(i, n):
                    if k % nums[j] != 0:
                        break
                    
                    cur_lcm = cur_lcm * nums[j] // math.gcd(cur_lcm, nums[j])
                    
                    if cur_lcm == k:
                        count += 1
                    elif cur_lcm > k:
                        break
            return count