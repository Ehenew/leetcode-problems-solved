class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False

        mismatch = []
        for a, b in zip(s1, s2):
            if a != b:
                mismatch.append((a,b))
        return len(mismatch) == 2 and mismatch[0] == mismatch[1][::-1]

            

            