class Solution(object):
    def restoreString(self, s, indices):
        shuffled_list = [''] * len(s)

        for index, char in zip(indices, s):
            shuffled_list[index] = char

        return ''.join(shuffled_list)