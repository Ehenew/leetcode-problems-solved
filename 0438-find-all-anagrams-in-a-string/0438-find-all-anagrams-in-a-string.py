from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        window_count = Counter(s[:len(p)])
        ans = []

        if window_count == p_count:
            ans.append(0)

        for i in range(len(p), len(s)):
            start_char = s[i - len(p)]
            new_char = s[i]

            window_count[new_char] += 1
            window_count[start_char] -= 1

            if window_count[start_char] == 0:
                del window_count[start_char]
            
            if window_count == p_count:
                ans.append(i - len(p) + 1) 
            
        return ans

    