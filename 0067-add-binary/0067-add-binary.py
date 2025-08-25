class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the result string and carry
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Traverse both strings from the end
        while i >= 0 or j >= 0 or carry:
            # Get the current digits, or 0 if the string is shorter
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Sum the digits and the carry
            total = digit_a + digit_b + carry
            
            # Append the current bit to the result
            result.append(str(total % 2))
            
            # Update the carry (0 or 1)
            carry = total // 2
            
            # Move to the next digits in the strings
            i -= 1
            j -= 1
        
        # The result list is in reverse order, so reverse it before returning
        return ''.join(result[::-1])
