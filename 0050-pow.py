class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1  # Base case: x^0 = 1
        if n < 0:
            x = 1 / x  # Invert x when n is negative
            n = -n  # Make n positive

        result = 1
        while n > 0:
            if n % 2 == 1:   
                result *= x
            x *= x   
            n //= 2  
        
        return result
