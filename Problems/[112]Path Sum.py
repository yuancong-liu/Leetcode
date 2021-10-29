# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        sumups = []
        sumup = 0
        self.pre(root, sumup, sumups)
        return (targetSum in sumups)

    def pre(self, root, sumup, sumups):
        sumup += root.val
        if root.left is None and root.right is None:
            sumups.append(sumup)
        if root.left is not None:
            self.pre(root.left, sumup, sumups)
        if root.right is not None:
            self.pre(root.right, sumup, sumups)
# leetcode submit region end(Prohibit modification and deletion)
