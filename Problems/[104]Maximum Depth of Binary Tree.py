# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        numbers = []
        length = ''
        self.pre(root, length, numbers)
        depth = 0
        for i in range(len(numbers)):
            if depth < len(numbers[i]):
                depth = len(numbers[i])
        return depth

    def pre(self, root, length, numbers):
        if root is None:
            return
        elif root.left is None and root.right is None:
            length += '1'
            numbers.append(length)
        length += '1'
        self.pre(root.left, length, numbers)
        self.pre(root.right, length, numbers)
# leetcode submit region end(Prohibit modification and deletion)
