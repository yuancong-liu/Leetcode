# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        means = []
        self.leveltra(root, means)
        return means

    def leveltra(self, root, means):
        if root is None:
            return
        myQueue = []
        level_num = [1]
        node = root
        # means.append(node.val)
        myQueue.append(node)
        i = 0
        while len(myQueue) != 0:
            count = 0
            sumup = 0
            if level_num[i] != 0:
                for j in range(level_num[i]):
                    node = myQueue.pop(0)
                    sumup += node.val
                    if node.left is not None:
                        myQueue.append(node.left)
                        count += 1
                    if node.right is not None:
                        myQueue.append(node.right)
                        count += 1
            level_num.append(count)
            if level_num[i] != 0:
                means.append(sumup / level_num[i])
            i += 1
# leetcode submit region end(Prohibit modification and deletion)
