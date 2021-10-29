# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numCountMap = Counter(nums)

        maximum = 0
        for num in nums:
            if num+1 in numCountMap:
                maximum = max(numCountMap[num] + numCountMap[num+1], maximum)

        return maximum

# leetcode submit region end(Prohibit modification and deletion)
