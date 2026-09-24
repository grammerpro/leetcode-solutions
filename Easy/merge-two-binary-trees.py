# Problem: Merge Two Binary Trees
# Topics: Trees
# Difficulty: Easy
# Evidence: Legacy (unverified)
# Link: https://leetcode.com/problems/merge-two-binary-trees/

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        result = TreeNode(root1.val + root2.val)
        stack = [(result, root1, root2)]
        while stack:
            merged, first, second = stack.pop()
            for side in ('left', 'right'):
                left, right = getattr(first, side), getattr(second, side)
                if left is None or right is None:
                    setattr(merged, side, right if left is None else left)
                else:
                    child = TreeNode(left.val + right.val)
                    setattr(merged, side, child)
                    stack.append((child, left, right))
        return result
