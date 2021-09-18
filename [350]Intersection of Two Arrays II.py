# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        intersection = []
        for num in nums2:
            if num in nums1:
                intersection.append(nums1.pop(nums1.index(num)))
        return intersection
# leetcode submit region end(Prohibit modification and deletion)
