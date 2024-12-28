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
        final = id
        graph = defaultdict(list)
        idtoimportance = {}
        for employee in employees:
            graph[employee.id] = [iid for iid in employee.subordinates]
            idtoimportance[employee.id] = employee.importance
        def calctotal(nodeid):
            total = 0
            q = deque()
            q.append(nodeid)
            while q:
                curr = q.popleft()
                total += idtoimportance[curr]
                for sub in graph[curr]:
                    q.append(sub)
                
            return total
        return calctotal(final)