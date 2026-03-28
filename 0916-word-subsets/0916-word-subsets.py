class Solution:
    def wordSubsets(self, words1, words2):
        from collections import Counter
        
        max_freq = Counter()
        
        for word in words2:
            freq = Counter(word)
            for ch in freq:
                max_freq[ch] = max(max_freq[ch], freq[ch])
        
        result = []
        
        for word in words1:
            freq = Counter(word)
            ok = True
            
            for ch in max_freq:
                if freq[ch] < max_freq[ch]:
                    ok = False
                    break
            
            if ok:
                result.append(word)
        return result