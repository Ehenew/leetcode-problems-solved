class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to help skip duplicates
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(list(path))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return result
      