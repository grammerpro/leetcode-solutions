# Problem: Binary Tree Level Order Traversal
# Topics: Trees
# Difficulty: Medium
# Evidence: Legacy (unverified)
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level)
        return result
