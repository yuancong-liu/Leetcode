# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = a = b = -10001
        for num in arr:
            a, b = max(a + num, num), max(b + num, a)
            ans = max(a, b, ans)

        return ans
# leetcode submit region end(Prohibit modification and deletion)
