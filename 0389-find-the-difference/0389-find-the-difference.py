class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq1 = {}
        freq2 = {}
        for char in s:
            freq1[char] = freq1.get(char, 0) + 1
        for char in t:
            freq2[char] = freq2.get(char, 0) + 1
        
        for char in t:
            if freq2[char] != freq1.get(char, 0):
                return char
            
