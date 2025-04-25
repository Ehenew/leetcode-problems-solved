class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result = []
        space_index = 0
        n = len(s)
        
        for i in range(n):
            if space_index < len(spaces) and i == spaces[space_index]:
                result.append(' ')  # Add space
                space_index += 1
            
            result.append(s[i])
        
        return ''.join(result)
