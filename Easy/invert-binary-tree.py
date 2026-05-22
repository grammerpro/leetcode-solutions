# Problem: Invert Binary Tree
# Topic: Trees
# Difficulty: Easy
# Link: https://leetcode.com/problems/invert-binary-tree/

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if tree is empty
        if not root:
            return None
            
        # Swap left and right children recursively
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        
        root.left = right_inverted
        root.right = left_inverted
        
        return root
