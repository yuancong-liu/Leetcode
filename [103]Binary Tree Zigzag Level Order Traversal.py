# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        output = []
        nextLayer = [root]
        flag = 0
        while nextLayer:
            nextNextLayer = []
            layerValue = []
            if flag == 1:
                for node in reversed(nextLayer):
                    if not node:
                        continue
                    layerValue.append(node.val)
                    if node.right:
                        nextNextLayer.append(node.right)
                    if node.left:
                        nextNextLayer.append(node.left)

                    flag = 0
            else:
                for node in reversed(nextLayer):
                    if not node:
                        continue
                    layerValue.append(node.val)
                    if node.left:
                        nextNextLayer.append(node.left)
                    if node.right:
                        nextNextLayer.append(node.right)
                    flag = 1

            nextLayer = nextNextLayer
            output.append(layerValue)
        return output

# leetcode submit region end(Prohibit modification and deletion)
