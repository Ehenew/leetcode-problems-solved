class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        tot_chemistry = 0
        team_skill = skill[0] + skill[-1]

        while left < right:
            if skill[left] + skill[right] != team_skill:
                return -1
            tot_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1

        return tot_chemistry