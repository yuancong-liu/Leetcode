# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        path1 = []
        path2 = []
        self.mid(p, path1)
        self.mid(q, path2)

        return path1 == path2

    def mid(self, root, path):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is not None:
            path.append(None)
        self.mid(root.left, path)
        self.mid(root.right, path)
        
# leetcode submit region end(Prohibit modification and deletion)
