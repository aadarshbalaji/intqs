class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        memo = {}
        visited = set()
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
            for n in graph[course]:
                if not cantake(n):
                    return False
            visited.remove(course)
            memo[course] = True
            return True
        
        for i in range(numCourses):
            if not cantake(i):
                return False
        return True
            
        