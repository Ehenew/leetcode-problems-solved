class Solution:
    def maxScore(self, s: str) -> int:
        s = list(s)

        left_count = 0
        right_count = 0
        max_count = 0

        for i in range(1, len(s)):
            left = s[0:i]
            right =s[i:]

            for j in range(len(left)):
                if left[j] == '0':
                    left_count += 1
            for j in range(len(right)):
                if right[j] == '1':
                    right_count += 1
                
            max_count = max(max_count, left_count + right_count)
            left_count = 0
            right_count = 0
        return max_count

