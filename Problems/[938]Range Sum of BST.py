# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.sumrange(root, low, high)

    def sumrange(self, root, low, high):
        if root is None:
            return 0
        sumup = 0
        if root.val >= low and root.val <= high:
            sumup += root.val
        sumup += self.sumrange(root.left, low, high)
        sumup += self.sumrange(root.right, low, high)
        return sumup
# leetcode submit region end(Prohibit modification and deletion)
