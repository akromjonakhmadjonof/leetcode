# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = height(node.left)
            if lh == -1:            # left already unbalanced
                return -1
            rh = height(node.right)
            if rh == -1:            # right already unbalanced
                return -1
            if abs(lh - rh) > 1:    # this node unbalanced
                return -1
            return 1 + max(lh, rh)  # return height if balanced

        return height(root) != -1
