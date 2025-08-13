class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        exponent = ''

        for n in b:
            exponent += str(n)
        
        num_exponent = int(exponent)

        return(pow(a, num_exponent, 1337))