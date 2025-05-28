import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        banned = set(banned)

        counts = {}
        max_count = 0
        result = ''

        for word  in words:
            if word not in banned:
                counts[word] = counts.get(word, 0) + 1
                if counts[word] > max_count:
                    max_count = max(max_count, counts[word])
                    result = word
        return result


