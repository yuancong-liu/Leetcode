# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = []
        self.pre(root, string)
        string = ''.join(string)
        return string

    def pre(self, root, string):
        if root is None:
            return
        string.append(str(root.val))
        if root.left is not None:
            string.append('(')
            self.pre(root.left, string)
            string.append(')')
        elif root.right is not None:
            string.append('(')
            string.append(')')
        if root.right is not None:
            string.append('(')
            self.pre(root.right, string)
            string.append(')')
# leetcode submit region end(Prohibit modification and deletion)
