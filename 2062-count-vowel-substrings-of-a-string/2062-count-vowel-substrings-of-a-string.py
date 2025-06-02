class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        count = 0

        for i in range(n):
            if word[i] not in vowels:
                continue
            unique_vowels = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                unique_vowels.add(word[j])
                if len(unique_vowels) == 5:
                    count += 1
        return count
