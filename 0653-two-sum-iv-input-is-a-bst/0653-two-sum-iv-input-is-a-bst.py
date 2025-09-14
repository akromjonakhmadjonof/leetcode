class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set() # Stores all visited node values
        
        def iterate(node):
            if not node:
                return False
            #  Have we seen a value that we can add to current value to get k ?
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return iterate(node.left) or iterate(node.right)
        
        return iterate(root)