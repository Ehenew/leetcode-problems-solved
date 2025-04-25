class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        nums_set = set()
        
        for num in arr:
            if num * 2 in nums_set or (num % 2 == 0 and num // 2 in nums_set):
                return True
            nums_set.add(num)
        
        return False
