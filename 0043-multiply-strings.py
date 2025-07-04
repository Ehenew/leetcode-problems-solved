class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Reverse loop for manual multiplication
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                pos1 = i + j
                pos2 = i + j + 1

                sum_ = mul + result[pos2]
                result[pos2] = sum_ % 10
                result[pos1] += sum_ // 10

        # Skip leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')
        return result_str or "0"
