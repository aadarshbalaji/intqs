class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vtoe = defaultdict(list)
        for course, prereq  in prerequisites:
            vtoe[course].append(prereq)

        memo = {}
        def check(course, relied):
            if course in memo:
                return memo[course]
            if len(vtoe[course]) == 0:
                memo[course] = True
                return memo[course]
            if course in relied:
                memo[course] = False
                return memo[course]
            new = relied + [course]
            for preq in vtoe[course]:
                if not check(preq, new):
                    memo[preq] = False
                    return False
            memo[course] = True
            return True
                

            

        for i in range((numCourses)):
            if not check(i, []):
                return False
        return True