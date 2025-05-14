class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_dict = {}

        for num in arr:
            my_dict[num] = my_dict.get(num, 0) + 1

        is_all_unique = len(set(my_dict.values())) == len(my_dict.values())

        return is_all_unique