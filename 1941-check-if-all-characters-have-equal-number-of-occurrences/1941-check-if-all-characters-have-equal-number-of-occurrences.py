class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_freq = {}

        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        return len(set(char_freq.values())) == 1