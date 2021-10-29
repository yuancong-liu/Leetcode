# leetcode submit region begin(Prohibit modification and deletion)
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
        checked = []
        employeeMap = {employee.id: employee for employee in employees}
        totalValue = 0

        def check(id):
            nonlocal totalValue
            nonlocal checked
            if id in checked:
                return
            totalValue += employeeMap[id].importance
            checked.append(id)
            if not employeeMap[id].subordinates:
                return
            for subordinate in employeeMap[id].subordinates:
                check(subordinate)

        check(id)

        return totalValue
# leetcode submit region end(Prohibit modification and deletion)
