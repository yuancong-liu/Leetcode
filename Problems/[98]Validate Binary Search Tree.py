# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        nums = []
        self.inOrder(root, nums)
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True

    def inOrder(self, root, nums: list):
        if root is None:
            return
        self.inOrder(root.left, nums)
        nums.append(root.val)
        self.inOrder(root.right, nums)
# leetcode submit region end(Prohibit modification and deletion)
