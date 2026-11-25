# Problem: Convert Binary Number in a Linked List to Integer
# Topics: Linked Lists
# Difficulty: Easy
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        value = 0
        while head:
            value = value * 2 + head.val
            head = head.next
        return value
