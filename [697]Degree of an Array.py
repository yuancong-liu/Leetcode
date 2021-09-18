# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequencies = Counter(nums)
        degree = max(frequencies.values())
        length = len(nums)
        mininmum = length
        smun = list(reversed(nums))
        numsDegree = [num for num in frequencies if frequencies[num] == degree]
        for num in numsDegree:
            mininmum = min(mininmum, length - nums.index(num) - smun.index(num))

        return mininmum
        
# leetcode submit region end(Prohibit modification and deletion)
