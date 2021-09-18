# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums) + 1)) - set(nums)).pop()
# leetcode submit region end(Prohibit modification and deletion)
