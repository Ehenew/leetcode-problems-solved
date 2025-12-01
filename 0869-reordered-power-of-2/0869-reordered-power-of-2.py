class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def signature(x):
            return tuple(sorted(str(x)))  
        sig = signature(n)

        for i in range(31):
            if signature(1 << i) == sig:
                return True
        return False