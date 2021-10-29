# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = []
        self.pre(root, values)
        # if k in values:
        #     return True
        for i in range(len(values) - 1):
            for j in range(i + 1, len(values)):
                if values[i] + values[j] == k:
                    return True
        return False

    def pre(self, root, values):
        if root is None:
            return
        values.append(root.val)
        self.pre(root.left, values)
        self.pre(root.right, values)
# leetcode submit region end(Prohibit modification and deletion)
