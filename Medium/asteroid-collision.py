# Problem: Asteroid Collision
# Topics: Stacks
# Difficulty: Medium
# Evidence: LeetCode Accepted
# Link: https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                if stack[-1] == -asteroid:
                    stack.pop()
                alive = False
            if alive:
                stack.append(asteroid)
        return stack
