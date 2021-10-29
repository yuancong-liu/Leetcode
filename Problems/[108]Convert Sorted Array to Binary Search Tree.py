# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(nums[int(len(nums) / 2)])
        self.add(root, nums)
        return root

    def add(self, root, arr):
        if len(arr) == 1:
            return
        if root is None:
            return
        mid = int(len(arr) / 2)
        submid_1 = int(mid / 2)
        submid_2 = int((len(arr) - 1 - mid) / 2) + mid + 1
        root.left = TreeNode(arr[submid_1])
        if submid_2 < len(arr):
            root.right = TreeNode(arr[submid_2])
        self.add(root.left, arr[:mid])
        self.add(root.right, arr[mid + 1:])
# leetcode submit region end(Prohibit modification and deletion)
