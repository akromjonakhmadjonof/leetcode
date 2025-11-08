# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}
        def bfs(node, level):
            if not node:
                return
            if level not in levels:
                levels[level] = []
            levels[level].append(node.val)
            level += 1
        
            bfs(node.left, level)
            bfs(node.right, level)
        bfs(root, 0)
        return list(levels.values())