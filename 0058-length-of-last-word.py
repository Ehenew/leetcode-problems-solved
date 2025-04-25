class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip() # Trim the string to remove trailing spaces
        
        words = s.split()
        
        return len(words[-1])
