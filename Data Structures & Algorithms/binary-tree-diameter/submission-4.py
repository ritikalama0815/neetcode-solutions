# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #since it doesnt have to always pass thru root, we can find the maximum among the sums of left and
        #right height
        #use dfs to compute the height of every subtree
        # and take max of left, right or left+right

        self.depth = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.depth = max(self.depth, left+right)
            return max(left,right)+1
        
        dfs(root)
        return self.depth

        