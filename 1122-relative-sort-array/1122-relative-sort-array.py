class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}

        for x in arr1:
            freq[x] = freq.get(x, 0) + 1
        
        result = []
        for x in arr2:
            if x in freq:
                result += [x] * freq[x]
                del freq[x]

        remaining = sorted(freq.keys())
        for x in remaining:
            result += [x] * freq[x]

        return result
