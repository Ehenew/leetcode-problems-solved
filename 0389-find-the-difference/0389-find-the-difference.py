class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:
            freq[char] = freq.get(char, 0) - 1
            if freq[char] < 0:
                return char
