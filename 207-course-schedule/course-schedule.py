class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courses = defaultdict(list)
        for course, prereq  in prerequisites:
            courses[course].append(prereq)

        visited = set()
        def dfs(c):
            # base case: reached course w/ no prereq
            if courses[c] == []:
                return True 
            
            if c in visited:
                return False
            
            visited.add(c) # 1, 2, 3
            # visit neighborssssss
            for n in courses[c]:
                if not dfs(n):
                    return False 
            # print("dfs: {} visited: {}".format(c, visited))
            visited.remove(c)
            # print("remove(c): {}".format(visited))

            courses[c] = []
            # print("courses[{}] = {}".format(c, courses[c]))
            return True 

        # for course in courses.keys():
        for i in range(numCourses):
            # call dfs on course to find cycle 
            if not dfs(i):
                return False
        return True 
