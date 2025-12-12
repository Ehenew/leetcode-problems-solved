class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        result = []

        for i, word in enumerate(sentence.split(), start=1):
            if word[0] in vowels:
                goat = word + "ma"
            else:
                goat = word[1:] + word[0] + "ma"

            goat += "a" * i
            result.append(goat)
        return " ".join(result)
