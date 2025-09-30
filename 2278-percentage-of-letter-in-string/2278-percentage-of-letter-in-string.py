class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = Counter(s)
        return count[letter] * 100 // len(s)