class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        ans = []
        for numlist in prerequisites:
            course = numlist[0]
            prereq = numlist[1]
            adj[prereq].append(course)
            indegree[course] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            t = q.popleft()
            ans.append(t)
            for nextcourse in adj[t]:
                indegree[nextcourse] -= 1
                if indegree[nextcourse] == 0:
                    q.append(nextcourse)
        
        return len(ans) == numCourses
        