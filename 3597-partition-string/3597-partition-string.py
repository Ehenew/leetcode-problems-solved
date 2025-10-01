class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        result = []
        curr = ""

        for ch in s:
            curr += ch
            if curr not in seen:      
                result.append(curr)   
                seen.add(curr)       
                curr = ""           
        return result
