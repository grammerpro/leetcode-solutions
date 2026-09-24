# Problem: Symmetric Tree
# Topics: Trees
# Difficulty: Easy
# Evidence: Legacy (unverified)
# Link: https://leetcode.com/problems/symmetric-tree/

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None or right is None:
                if left is not right:
                    return False
                continue
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True
