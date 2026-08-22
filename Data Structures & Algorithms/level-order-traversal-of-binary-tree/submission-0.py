# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = []

        def dfs(root, d):
            if not root:
                return None
            if len(level) == d:
                level.append([])

            level[d].append(root.val)
            dfs(root.left, d+1)
            dfs(root.right, d+1)
        
        dfs(root, 0)
        return level