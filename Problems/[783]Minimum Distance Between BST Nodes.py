# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []
        self.pre(root, values)
        min = 10 ** 5
        for i in range(len(values) - 1):
            ab = values[i + 1] - values[i]
            if ab < min:
                min = ab
        return min

    def pre(self, root, values):
        if root is None:
            return
        self.pre(root.left, values)
        values.append(root.val)
        self.pre(root.right, values)
# leetcode submit region end(Prohibit modification and deletion)
