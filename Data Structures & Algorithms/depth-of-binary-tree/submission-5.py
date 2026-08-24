# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if there is no root, return 0
        if not root:
            return 0
        # recursively find the depth of left and right subtrees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # return the maximum of left or right depth
        depth = max(left, right)
        # add 1 to find nodes
        return 1+depth
        