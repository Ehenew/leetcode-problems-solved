class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        words = sentence.split()
        dictionary_set = set(dictionary)

        for i, word in enumerate(words):
            for j in range(1,len(word) + 1):
                prefix = word[:j]
                if prefix in dictionary_set:
                    words[i] = prefix

        return ' '.join(words)