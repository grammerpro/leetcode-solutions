# Problem: Maximum Depth of Binary Tree
# Topic: Trees
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: empty tree has depth 0
        if not root:
            return 0
            
        # Recursively find the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return max(left_depth, right_depth) + 1
