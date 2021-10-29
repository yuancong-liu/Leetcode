# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        path = ''
        self.pre(root, path, paths)
        return paths

    def pre(self, root, path, paths):
        if root is None:
            return
        elif root.left is None and root.right is None:
            path += str(root.val)
            paths.append(path)
        path += str(root.val)
        path += str("->")
        self.pre(root.left, path, paths)
        self.pre(root.right, path, paths)
# leetcode submit region end(Prohibit modification and deletion)
