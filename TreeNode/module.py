class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def dfs(root, depth):
        if not root:
            return depth
        else:
            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))
