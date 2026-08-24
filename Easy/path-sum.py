# Problem: Path Sum
# Topic: Trees
# Difficulty: Easy
# Link: https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Check base cases
        if not root:
            return False
            
        # If it is a leaf node, check value match
        if not root.left and not root.right:
            return targetSum == root.val
            
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
