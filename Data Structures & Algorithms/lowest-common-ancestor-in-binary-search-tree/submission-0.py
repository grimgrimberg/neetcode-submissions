# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if root is None:
        #     return root
        #in bst left is smaller than father, right is bigger. so logic should have it.
        head = root
        while head:
            if head.val < q.val and p.val> head.val:
                head = head.right
                # lowestCommonAncestor(head.right,p,q)
            if head.val > q.val and p.val < head.val:
                head = head.left
                # lowestCommonAncestor(head.left,p,q)
            else:
                return head
        # if head.left is p or head.right is p and head.left is q or head.right is q or head.val == p.val or head.val == q.val:
        # # if head.left is p or head.right is p and head.left is q or head.right is q: 
        # # if (head.left or head.right) is p and (head.left or head.right) is q or head.val == p.val or head.val == q.val:
        #     return head
        


        # while root:
        #     if (root.left or root.right) is p and (root.left or root.right) is q or root.val is p or root.val is q
        #         return root.val
        #     self.lowestCommonAncestor(root.left,p,q)
        #     self.lowestCommonAncestor(root.right,p,q)
        
        # return root

            
            
            