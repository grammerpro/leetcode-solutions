# Problem: Car Pooling
# Topics: Intervals
# Difficulty: Medium
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [0] * 1002
        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers
        riding = 0
        for change in changes:
            riding += change
            if riding > capacity:
                return False
        return True
