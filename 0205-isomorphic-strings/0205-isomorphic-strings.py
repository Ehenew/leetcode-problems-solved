class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = {}
        t_mapped = set()

        for char_s, char_t in zip(s, t):
            if char_s in mapping:
                if mapping[char_s] != char_t:
                    return False
            else:
                if char_t in t_mapped:
                    return False
                mapping[char_s] = char_t
                t_mapped.add(char_t)
        return True

        