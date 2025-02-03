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
            if len(graph[num]) == 0:
                memo[num] = True
                return True
            if num in seen:
                return False
            seen.add(num)
            b = True
            for pre in graph[num]:
                b = b and cantake(pre)
            memo[num] = b
            return b 
        for i in range(numCourses):
            if not cantake(i):
                return False
        return True
            