class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = list(words[0])
    
        for word in words[1:]:
            new_res = []
            word_list = list(word)
            for ch in res:
                if ch in word_list:
                    new_res.append(ch)
                    word_list.remove(ch)  
            res = new_res
            
        return res