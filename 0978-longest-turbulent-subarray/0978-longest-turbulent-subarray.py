class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n

        max_len = 1
        left = 0
        prev_comp = None

        for right in range(1, n):
            if arr[right - 1] > arr[right]:
                current_comp = '>'
            elif arr[right - 1] < arr[right]:
                current_comp = '<'
            else:
                # Equal elements break turbulence
                left = right
                prev_comp = None
                continue

            if prev_comp and current_comp == prev_comp:
                # No flip — reset window
                left = right - 1

            prev_comp = current_comp
            max_len = max(max_len, right - left + 1)

        return max_len
