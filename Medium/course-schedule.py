# Problem: Course Schedule
# Topics: Graphs
# Difficulty: Medium
# Evidence: LeetCode Accepted
# Link: https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        following = [[] for _ in range(numCourses)]
        waiting = [0] * numCourses
        for course, required in prerequisites:
            following[required].append(course)
            waiting[course] += 1
        ready = [course for course in range(numCourses) if waiting[course] == 0]
        finished = 0
        while ready:
            course = ready.pop()
            finished += 1
            for later in following[course]:
                waiting[later] -= 1
                if waiting[later] == 0:
                    ready.append(later)
        return finished == numCourses
