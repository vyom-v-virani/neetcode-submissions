class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right)+1
        return dfs(root) != -1