# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        numbers = []
        number = ''
        self.pre(root, number, numbers)
        return sum(numbers)

    def pre(self, root, number, numbers):
        if root is None:
            return
        elif root.left is None and root.right is None:
            number += str(root.val)
            numbers.append(int(number, 2))
        number += str(root.val)
        self.pre(root.left, number, numbers)
        self.pre(root.right, number, numbers)
# leetcode submit region end(Prohibit modification and deletion)
