class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        my_dict = {}
        

        for word in s1.split():
            my_dict[word] = my_dict.get(word, 0) + 1
        for word in s2.split():
            my_dict[word] = my_dict.get(word, 0) + 1


    
        ans = [word for word in my_dict if my_dict[word] == 1]
        return ans
        
            
        