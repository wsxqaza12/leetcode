# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def DFS(node, l):
            if node is None: return
            if node.left is None and node.right is None:
                l.append(node.val)
            DFS(node.left, l)
            DFS(node.right, l)

        root_1 = []
        root_2 = []
        DFS(root1, root_1)
        DFS(root2, root_2)
        return root_1 == root_2
