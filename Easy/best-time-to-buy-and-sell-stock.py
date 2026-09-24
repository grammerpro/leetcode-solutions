# Problem: Best Time to Buy and Sell Stock
# Topics: Arrays
# Difficulty: Easy
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, best = prices[0], 0
        for price in prices:
            lowest = min(lowest, price)
            best = max(best, price - lowest)
        return best
