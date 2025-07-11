class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []

        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1

        res.extend(word1[i:])
        res.extend(word2[j:])
        return ''.join(res)
