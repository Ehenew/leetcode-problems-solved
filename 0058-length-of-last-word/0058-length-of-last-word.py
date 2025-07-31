class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Trim the string to remove trailing spaces
        s = s.strip()
        
        # Step 2: Split the string by spaces and get the last word
        words = s.split()
        
        # Step 3: Return the length of the last word
        return len(words[-1])
