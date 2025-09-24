# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0

            left_sum = 0
            # check if the left child is a leaf
            if node.left and not node.left.left and not node.left.right:
                left_sum += node.left.val

            # recurse into both children
            return left_sum + dfs(node.left) + dfs(node.right)

        return dfs(root)
