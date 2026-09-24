# Problem: Path Sum
# Topics: Trees
# Difficulty: Easy
# Evidence: Legacy (unverified)
# Link: https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = [(root, root.val)] if root is not None else []
        while stack:
            node, total = stack.pop()
            if node.left is None and node.right is None and total == targetSum:
                return True
            if node.left is not None:
                stack.append((node.left, total + node.left.val))
            if node.right is not None:
                stack.append((node.right, total + node.right.val))
        return False
