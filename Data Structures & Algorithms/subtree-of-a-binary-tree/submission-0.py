# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper1(root1, root2):
            if not root1 and not root2:
                return 1
            elif not root1:
                return 0
            elif not root2:
                return 0
            left = helper1(root1.left, root2.left)
            right = helper1(root1.right, root2.right)
            if right == 0 or left == 0:
                return 0
            return 1 if root1.val == root2.val else 0
        def helper2(root, sub):
            if not root:
                return 0
            val = helper1(root, sub)
            left = helper2(root.left, sub)
            right = helper2(root.right, sub)

            return max(val,left,right) == 1
        return helper2(root, subRoot) == 1
            

            







