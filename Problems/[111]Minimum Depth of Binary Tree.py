# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depths = []
        depth = 0
        self.pre(root, depth, depths)
        return min(depths)

    def pre(self, root, depth, depths):
        depth += 1
        if root.left is None and root.right is None:
            depths.append(depth)
        if root.left is not None:
            self.pre(root.left, depth, depths)
        if root.right is not None:
            self.pre(root.right, depth, depths)
# leetcode submit region end(Prohibit modification and deletion)
