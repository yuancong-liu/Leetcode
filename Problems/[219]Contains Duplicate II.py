# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numIndexMap = {}
        for i in range(len(nums)):
            if nums[i] not in numIndexMap:
                numIndexMap[nums[i]] = i
            else:
                if i - numIndexMap[nums[i]] <= k:
                    return True
                else:
                    numIndexMap[nums[i]] = i
        return False
# leetcode submit region end(Prohibit modification and deletion)
