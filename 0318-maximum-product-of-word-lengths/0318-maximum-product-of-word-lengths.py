class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        word_lens = [len(word) for word in words] 
        
        for i, word in enumerate(words):
            mask = 0 # 00000000
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            masks[i] = mask
        
        max_prod = 0
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0: 
                    curr_prod = word_lens[i] * word_lens[j]
                    max_prod = max(max_prod, curr_prod)
        
        return max_prod