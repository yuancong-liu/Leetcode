# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    balance = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.pre(root)
        return self.balance

    def pre(self, root):
        if not root:
            return 0
        height_left = self.pre(root.left)
        height_right = self.pre(root.right)
        if abs(height_right - height_left) > 1:
            self.balance = False
        return max(height_right, height_left) + 1

        
# leetcode submit region end(Prohibit modification and deletion)
