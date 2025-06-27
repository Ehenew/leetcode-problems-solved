"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_dict = {emp.id: emp for emp in employees}

        def dfs(emp_id, visited):
            if emp_id not in emp_dict or emp_id in visited:
                return 0

            visited.add(emp_id)
            tot = emp_dict[emp_id].importance
            for sub_id in emp_dict[emp_id].subordinates:
                tot += dfs(sub_id, visited)
            return tot
        
        return dfs(id, set())
