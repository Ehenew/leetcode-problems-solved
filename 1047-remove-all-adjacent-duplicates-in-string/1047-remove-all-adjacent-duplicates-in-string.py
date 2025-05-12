class Solution:
    def removeDuplicates(self, s: str) -> str:

        s = list(s)

        left = 0
        right = 1

        while s and right <= len(s):
            if s[right] == s[left]:
                s[left] = ''
                s[right] = ''
            else:
                left += 1
                right+= 1
        return ''.join(s)
            
        