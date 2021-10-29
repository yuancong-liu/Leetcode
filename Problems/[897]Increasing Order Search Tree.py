# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        numbers = []
        self.pre(root, numbers)

        root2 = TreeNode(numbers[0])
        head = root2
        for i in range(1, len(numbers)):
            head.right = TreeNode(numbers[i])
            head = head.right

        return root2

    def pre(self, root, numbers):
        if root is None:
            return
        self.pre(root.left, numbers)
        numbers.append(root.val)
        self.pre(root.right, numbers)
# leetcode submit region end(Prohibit modification and deletion)
