# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                nums.append(None)
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] is not None:
                k += 1

        return k
# leetcode submit region end(Prohibit modification and deletion)
