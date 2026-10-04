# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. If both are empty, they match perfectly so far
        if not p and not q:
            return True
                
            # 2. If only ONE is empty (but not both), they don't match
        if not p or not q:
            return False
                
            # 3. If the numbers inside don't match, they aren't the same
        if p.val != q.val:
            return False
                
            # 4. If we passed all those checks, ask the children to keep checking!
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


