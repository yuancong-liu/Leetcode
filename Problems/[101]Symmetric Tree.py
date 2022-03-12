# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)

# leetcode submit region end(Prohibit modification and deletion)
