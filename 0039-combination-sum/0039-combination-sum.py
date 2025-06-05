class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current_comb, current_sum):
            if current_sum == target:
                result.append(list(current_comb))
                return
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                current_comb.append(candidates[i])
                backtrack(i, current_comb, current_sum + candidates[i])
                current_comb.pop()  # backtrack

        backtrack(0, [], 0)
        return result
