# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndexMap = {}
        for index, value in enumerate(inorder):
            inorderIndexMap[value] = index

        preorderIndex = 0

        def addNode(left, right):
            nonlocal preorderIndex
            if left > right:
                return None

            rootValue = preorder[preorderIndex]
            root = TreeNode(rootValue)

            preorderIndex += 1

            root.left = addNode(left, inorderIndexMap[rootValue] - 1)
            root.right = addNode(inorderIndexMap[rootValue] + 1, right)

            return root

        return addNode(0, len(preorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)
