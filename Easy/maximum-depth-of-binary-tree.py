# Problem: Maximum Depth of Binary Tree
# Topics: Trees
# Difficulty: Easy
# Evidence: Legacy (unverified)
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        stack = [(root, 1)]
        while stack:
            node, current = stack.pop()
            depth = max(depth, current)
            if node.left is not None:
                stack.append((node.left, current + 1))
            if node.right is not None:
                stack.append((node.right, current + 1))
        return depth
