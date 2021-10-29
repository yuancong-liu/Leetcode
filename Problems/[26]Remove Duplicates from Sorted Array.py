# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        count = 0

        while i < len(nums) - 1:
            if count >= len(nums):
                break
            if nums[i] == nums[i + 1]:
                nums.append(nums.pop(i + 1))
            elif nums[i] < nums[i + 1]:
                i += 1
            else:
                break
            count += 1

        for k in range(len(nums) - 1):
            if nums[k] >= nums[k + 1]:
                return k + 1
# leetcode submit region end(Prohibit modification and deletion)
