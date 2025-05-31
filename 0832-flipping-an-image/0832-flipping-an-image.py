class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def reverse(arr):
            left = 0
            right = len(arr) -1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return arr

        def invert(arr):
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    arr[i] = 0 
            return arr
    
        n = len(image)
        result = []
        for i in range(n):
            row = reverse(image[i])
            row = invert(row)
            result.append(row)

        return result



