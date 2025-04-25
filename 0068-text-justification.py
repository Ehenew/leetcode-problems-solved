class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                total_spaces = maxWidth - current_length
                if len(current_line) == 1:
                    result.append(current_line[0] + ' ' * total_spaces)
                else:
                    spaces_between_words = total_spaces // (len(current_line) - 1)
                    extra_spaces = total_spaces % (len(current_line) - 1)
                    
                    line = current_line[0]
                    for i in range(1, len(current_line)):
                        spaces = ' ' * (spaces_between_words + (1 if i <= extra_spaces else 0))
                        line += spaces + current_line[i]
                    
                    result.append(line)
                
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word)
        
        last_line = ' '.join(current_line)
        result.append(last_line + ' ' * (maxWidth - len(last_line)))
        
        return result
