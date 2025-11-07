"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        results = []
        def helper(node):
            if not node:
                return
            results.append(node.val)
            children = node.children
            for child in children:
                helper(child)
        helper(root)
        return results