class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_count = sum(1 for char in word if char.isupper())

        if capital_count == len(word):
            return True
        elif capital_count == 0:
            return True
        elif capital_count == 1 and word[0].isupper():
            return True

        return False
