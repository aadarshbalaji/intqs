class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        path = []
        memo = {}
        def cantake(course, visited):
            if course in memo:
                return memo[course]
            if course in visited:
                return False
            if not graph[course]:
                path.append(course)
                memo[course] = True
                return True
            visited.add(course)
            for nxt in graph[course]:
                if not cantake(nxt, visited):
                    return False
            visited.remove(course)
            path.append(course)
            memo[course] = True
            return True
            

        for i in range(numCourses):
            if not cantake(i, set()):
                return []
        return path
            