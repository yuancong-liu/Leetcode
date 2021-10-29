# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.pre(root, values)
        return values

    def pre(self, root, values):
        if root is None:
            return
        values.append(root.val)
        self.pre(root.left, values)
        self.pre(root.right, values)
# leetcode submit region end(Prohibit modification and deletion)
