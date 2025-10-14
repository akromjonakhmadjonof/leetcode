class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = {}

        def helper(node, depth):
            if not node:
                return
            if depth not in levels:
                levels[depth] = []
            levels[depth].append(node.val)
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)

        helper(root, 0)
        return [sum(v) / len(v) for v in levels.values()]
