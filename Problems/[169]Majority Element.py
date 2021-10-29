# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numTimeMap = {}
        for num in nums:
            if num not in numTimeMap.keys():
                count = nums.count(num)
                numTimeMap[num] = count
                if count > len(nums) / 2:
                    return num
# leetcode submit region end(Prohibit modification and deletion)
