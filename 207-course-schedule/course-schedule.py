import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        """
        cycle detection with kahn's algorithm
        """
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = set()
        memo = {}
        def cantake(course):
            if not graph[course]:
                memo[course] = True
                return True
            if course in memo:
                return memo[course]
            if course in visited:
                memo[course] = False
                return False
            visited.add(course)
            result = [cantake(clas) for clas in graph[course]]
            memo[course] = all(result)
            return all(result)
        return all([cantake(i) for i in range(numCourses)])