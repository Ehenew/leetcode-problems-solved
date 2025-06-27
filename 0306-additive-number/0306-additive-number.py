class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def backtrack(start, path):
            if start == len(num) and len(path) >= 3:
                return True

            for end in range(start + 1, len(num) + 1):
                curr = num[start:end]

                if len(curr) > 1 and curr[0] == '0':
                    break

                curr_num = int(curr)

                if len(path) >= 2 and path[-1] + path[-2] != curr_num:
                    continue

                path.append(curr_num)
                if backtrack(end, path):
                    return True
                path.pop()

            return False
        return backtrack(0, [])


        