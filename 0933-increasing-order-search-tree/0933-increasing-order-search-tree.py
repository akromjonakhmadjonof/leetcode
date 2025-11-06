# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        values.sort(reverse=True)
        dummy = TreeNode(0)
        current = dummy
        while len(values) > 0:
            current.right = TreeNode(values.pop())
            current = current.right
            
        return dummy.right