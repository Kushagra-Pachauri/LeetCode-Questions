class Solution:
    def postorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)       # Left
            dfs(node.right)      # Right
            result.append(node.val)  # Root

        dfs(root)
        return result