# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(root, node, path):
            if root == None:
                return None
            if root.val == node.val:
                return path + [root]
            left_path = helper(root.left, node, path+ [root])
            if left_path:
                return left_path
            right_path = helper(root.right, node, path + [root])
            if right_path:
                return right_path
            return None

                
        if root.val == p.val or root.val == q.val:
            return root
        i = 0
        path1 = helper(root, p, [])
        path2 = helper(root, q , [])
        print(path1 , path2)
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            i+=1
        return path1[i-1]
