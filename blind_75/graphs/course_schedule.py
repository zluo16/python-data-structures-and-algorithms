import time
from typing import Dict, List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        c_map = self.create_course_map_from_edges(prerequisites, numCourses)
        visited = set()
        for k in c_map.keys():
            if not self.dfs(c_map, k, visited):
                return False

        return True

    def create_course_map_from_edges(self, prerequisites: List[List[int]], num_courses: int) -> Dict:
        c_map = {}
        for c in range(num_courses):
            c_map[c] = []

        for course in prerequisites:
            c_map[course[0]].append(course[1])

        return c_map

    def dfs(self, course_map: Dict[int, list], key: int, visited: Set[int]) -> bool:
        if key in visited:
            return False

        if len(course_map[key]) == 0:
            return True

        visited.add(key)
        for k in course_map[key]:
            if not self.dfs(course_map, k, visited):
                return False

        visited.remove(key)
        course_map[key] = []

        return True


c1 = [[1, 0]]
c2 = [[1, 0], [0, 1]]
c3 = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
c4 = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.canFinish(2, c1))
    print(sol.canFinish(2, c2))
    print(sol.canFinish(5, c3))
    print(sol.canFinish(20, c4))
    print("----%s seconds----" % (time.time() - start_time))
