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
        seen = set()
        def cantake(num):
            if num in memo:
                return memo[num]
            if num in seen:
                memo[num] = False
                return False
            if len(graph[num]) == 0:
                memo[num] = True
                return True
            seen.add(num)
            for pre in graph[num]:
                if not cantake(pre):
                    memo[num] = False
                    return False
            memo[num] = True
            return True
        
        for i in range(numCourses):
            if not cantake(i):
                return False
        return True