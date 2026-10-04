# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        # temp = root.left
        # root.left = root.right
        # root.rght = temp
        depth_left = self.maxDepth(root.left)
        # depth +=1
        depth_right = self.maxDepth(root.right)
        # depth +=1
        return max(depth_left,depth_right) +1
        # while root:
        #     root = root.left
        #     depth +=1
        #     if not root.left:
        #         root = root.right
        #         depth +=1
            
        # depth +=1
        # return depth