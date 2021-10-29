# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        numbers = []
        self.pre(root, numbers)
        for i in range(len(numbers) - 1):
            if numbers[i] != numbers[i + 1]:
                return False
        return True

    def pre(self, root, numbers):
        if root is None:
            return
        numbers.append(root.val)
        self.pre(root.left, numbers)
        self.pre(root.right, numbers)
# leetcode submit region end(Prohibit modification and deletion)
