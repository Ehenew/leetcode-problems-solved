from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""
        counts = Counter(s)
        items_sorted = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return ''.join(char * freq for char, freq in items_sorted)