# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(root1, root2):
            if not root1 and not root2:
                return 1
            elif not root1:
                return 0
            elif not root2:
                return 0
            left = helper(root1.left, root2.left)
            right = helper(root1.right, root2.right)
            if right == 0 or left == 0:
                return 0
            return 1 if root1.val == root2.val else 0
        ans = helper(p,q)
        return ans == 1