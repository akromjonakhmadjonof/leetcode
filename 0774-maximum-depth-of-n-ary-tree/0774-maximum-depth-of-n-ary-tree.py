"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node, depth):
            if not node:
                return depth
            children = node.children
            depth += 1
            if not children:
                return depth
            max_depth = depth
            for child in children:
                max_depth = max(max_depth, dfs(child, depth))
            return max_depth
            
        return dfs(root, 0)
