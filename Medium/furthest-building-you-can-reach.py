# Problem: Furthest Building You Can Reach
# Topics: Heaps
# Difficulty: Medium
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/furthest-building-you-can-reach/

import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Ladders cover the largest climbs seen so far; bricks pay for the rest.
        largest_climbs = []
        for index in range(len(heights) - 1):
            climb = heights[index + 1] - heights[index]
            if climb <= 0:
                continue
            heapq.heappush(largest_climbs, climb)
            if len(largest_climbs) > ladders:
                bricks -= heapq.heappop(largest_climbs)
                if bricks < 0:
                    return index
        return len(heights) - 1
