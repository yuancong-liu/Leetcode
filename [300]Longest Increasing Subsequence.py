# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dynamicLength = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            maximum = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maximum = max(maximum, dynamicLength[j] + 1)

            dynamicLength[i] = maximum

        return max(dynamicLength)
# leetcode submit region end(Prohibit modification and deletion)
