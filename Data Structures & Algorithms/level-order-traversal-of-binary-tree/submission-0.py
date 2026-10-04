# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []
        head = root
        if root is None:
            return []
        q = deque([root])
        while q:
            level = []
            len_level = len(q)
            for _ in range(len_level):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    # self.levelOrder(node.left)
                    q.append(node.left)
                if node.right:
                    # self.levelOrder(node.right)
                    q.append(node.right)

            sol.append(level)
        return sol


