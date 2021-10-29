# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        top = prices[0]
        bottom = prices[0]
        for price in prices:
            bottom = min(price, bottom)
            top = max(price, bottom)
            maximumProfit = max(maximumProfit, top - bottom)

        return maximumProfit
# leetcode submit region end(Prohibit modification and deletion)
