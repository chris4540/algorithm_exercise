

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        ret = []

        queue = [root]
        level = 0
        while queue:
            row = []
            row_vals = []
            # each while loop should be one level
            for node in queue:
                row_vals.append(node.val)
                if node.left:
                    row.append(node.left)
                if node.right:
                    row.append(node.right)
            queue = row

            if level % 2 == 1:
                row_vals = row_vals[::-1]

            ret.append(row_vals)

            # going to next level
            level += 1

        return ret



