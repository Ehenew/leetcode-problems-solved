class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            # Sort the word and use the sorted word as the key
            sorted_word = ''.join(sorted(word))
            
            # Group anagrams using the sorted word as the key
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
