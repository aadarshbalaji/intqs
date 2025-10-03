class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        arr = []
        memo = {}
        def cantake(course, visited):
            if course in memo:
                return memo[course]
            if course in visited:
                return False
            if not graph[course]:
                arr.append(course)
                memo[course] = True
                return True
            visited.add(course)
            for pre in graph[course]:
                if not cantake(pre, visited):
                    return False
            visited.remove(course)
            arr.append(course)
            memo[course] = True
            return True
        
        for i in range(numCourses):
            if not cantake(i, set()):
                return []
        return arr
            