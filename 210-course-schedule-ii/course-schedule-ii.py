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

        memo = {}
        ans = []
        def cantake(course, visited):
            if course in memo:
                return memo[course]
            
            if course in visited:
                memo[course] = False
                return False
            
            if not graph[course]:
                ans.append(course)
                memo[course] = True
                return True
            
            visited.add(course)
            for test in graph[course]:
                if not cantake(test,  visited):
                    return False
            visited.remove(course)
            memo[course] = True
            ans.append(course)
            return True
        
        for i in range(numCourses):
            if not cantake(i,set()):
                return []
        return ans