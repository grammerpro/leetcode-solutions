# Problem: Insert Interval
# Topics: Intervals
# Difficulty: Medium
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        before, after = [], []
        for interval in intervals:
            if interval[1] < start:
                before.append(interval)
            elif interval[0] > end:
                after.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        return before + [[start, end]] + after
