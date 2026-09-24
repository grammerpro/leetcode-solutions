# Problem: Subtree of Another Tree
# Topics: Trees
# Difficulty: Easy
# Evidence: Legacy (unverified)
# Link: https://leetcode.com/problems/subtree-of-another-tree/

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(first, second):
            pairs = [(first, second)]
            while pairs:
                left, right = pairs.pop()
                if left is None or right is None:
                    if left is not right:
                        return False
                    continue
                if left.val != right.val:
                    return False
                pairs.append((left.left, right.left))
                pairs.append((left.right, right.right))
            return True

        if subRoot is None:
            return True
        stack = [root] if root is not None else []
        while stack:
            node = stack.pop()
            if node.val == subRoot.val and same(node, subRoot):
                return True
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return False
