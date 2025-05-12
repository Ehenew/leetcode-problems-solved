from collections import Counter
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {
            'row1': 'qwertyuiop',
            'row2': 'asdfghjkl',
            'row3': 'zxcvbnm',
        }
        result = []
        
        for word in words:
            lower_word = set(word.lower())
            if lower_word.issubset(rows['row1']) or \
                lower_word.issubset(rows['row2']) or \
                lower_word.issubset(rows['row3']):
                result.append(word)
        return result
    




