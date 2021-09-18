# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 = cost[0]
        prev2 = cost[1]
        for i in range(2, len(cost)):
            tmp = cost[i] + min(prev1, prev2)
            prev1 = prev2
            prev2 = tmp
        return min(prev1, prev2)

# leetcode submit region end(Prohibit modification and deletion)
