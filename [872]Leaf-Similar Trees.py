# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = []
        seq2 = []
        self.pre(root1, seq1)
        self.pre(root2, seq2)
        return seq1 == seq2

    def pre(self, root, seq):
        if root is None:
            return
        if root.left is None and root.right is None:
            seq.append(root.val)
        self.pre(root.left, seq)
        self.pre(root.right, seq)
# leetcode submit region end(Prohibit modification and deletion)
