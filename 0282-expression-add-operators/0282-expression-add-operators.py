class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def dfs(idx, prev, curr_val, path):
            if idx == n:
                if curr_val == target:
                    res.append(path)
                return

            for i in range(idx, n):
                if i > idx and num[idx] == '0':
                    break

                operand_str = num[idx:i + 1]
                operand = int(operand_str)

                if idx == 0:
                    dfs(i + 1, operand, operand, operand_str)
                else:
                    dfs(i + 1, operand, curr_val + operand, path + "+" + operand_str)
                    dfs(i + 1, -operand, curr_val - operand, path + "-" + operand_str)
                    dfs(i + 1, prev * operand, curr_val - prev + (prev * operand),
                        path + "*" + operand_str)

        dfs(0, 0, 0, "")
        return res
