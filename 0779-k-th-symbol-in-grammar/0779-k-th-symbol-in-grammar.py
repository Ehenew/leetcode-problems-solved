class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        # 0
        # 01
        # 0110
        # 01101001

        # n = 2
        # k = 2

        if n == 1:
            return 0        

        current = self.kthGrammar(n - 1, (k + 1) // 2 )

        if k % 2 != 0:
            return current
        else:
            return 1 - current