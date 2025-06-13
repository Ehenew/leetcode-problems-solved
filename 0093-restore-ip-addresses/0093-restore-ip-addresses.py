class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def helper(start, path):

            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
                # 25525511135
            for i in range(1, 4):
                if start + i > len(s):
                    break

                comb = s[start:start + i]

                if (comb.startswith("0") and len(comb) > 1) or int(comb) > 255:
                    continue
            
                path.append(comb)
                helper(start + i,path )
                path.pop()

        helper(0, [])

        return res

            