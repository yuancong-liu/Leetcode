# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            for i in range(len(nums) - 1):
                if nums[i] < target < nums[i + 1]:
                    return i + 1
# leetcode submit region end(Prohibit modification and deletion)
