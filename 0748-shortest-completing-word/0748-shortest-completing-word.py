from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        need = Counter(c.lower() for c in licensePlate if c.isalpha())
        ans = None

        for w in words:
            cnt = Counter(w.lower())
            ok = True
            for c in need:
                if cnt[c] < need[c]:
                    ok = False
                    break
            if ok:
                if ans is None or len(w) < len(ans):
                    ans = w
        return ans