# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        node = root.left
        root.left = root.right
        root.right = node
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
# leetcode submit region end(Prohibit modification and deletion)
