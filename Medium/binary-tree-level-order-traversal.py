# Problem: Binary Tree Level Order Traversal
# Topic: Trees
# Difficulty: Medium
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS traversal keeping track of child elements at each level
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(level)
        return res
