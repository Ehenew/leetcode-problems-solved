class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        s = list(s)

        for _ in range(len(s)):
            first = s.pop(0)
            s.append(first)

            if ''.join(s) == goal:
                return True
        return False
