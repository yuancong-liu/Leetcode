# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        original = Counter({num + 1: 3 for num in range(len(nums))})
        counter = Counter(nums)

        diff = original - counter
        ans = [0, 0]
        for item in diff.keys():
            if diff[item] == 1:
                ans[0] = item
                continue
            if diff[item] == 3:
                ans[1] = item
                continue

        return ans
# leetcode submit region end(Prohibit modification and deletion)
