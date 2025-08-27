class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def dfs(i, prev, cnt):
            if i == n and cnt >= 2:
                return True

            temp_num = 0
            for j in range(i, n):
                temp_num = temp_num * 10 + int(s[j])
                if prev is None or temp_num == prev - 1:
                    if dfs(j + 1, temp_num, cnt + 1):
                        return True

                if prev is not None and temp_num >= prev:
                    break
            return False

        return dfs(0, None, 0)

    
