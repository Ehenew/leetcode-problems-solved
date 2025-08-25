class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_num = bin(x ^ y)

        # print(bin_num) #0b101
        ans = 0
        for i in range(2, len(bin_num)):
            if bin_num[i] == '1':
                ans += 1
        return ans

