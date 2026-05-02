# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return 
            curr = root
            left = curr.left
            right = curr.right
            if right and left:
                curr.left,curr.right = right,left
            elif not right:
                curr.right = left
                curr.left = None
            elif not left:
                curr.left = right
                curr.right = None
            helper(curr.left)
            helper(curr.right)
        helper(root)
        return root

                    