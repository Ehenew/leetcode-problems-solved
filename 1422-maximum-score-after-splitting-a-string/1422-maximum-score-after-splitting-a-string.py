class Solution:
    def maxScore(self, s: str) -> int:        
        max_count = 0

        for i in range(1, len(s)):
            left = s[0:i]
            right =s[i:]
                
            left_count = left.count('0')
            right_count = right.count('1')

            max_count = max(max_count, left_count + right_count)
        return max_count

