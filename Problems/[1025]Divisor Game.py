# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def divisorGame(self, n: int) -> bool:
        resultMap = [False for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0 and resultMap[i - j] is False:
                    resultMap[i] = True
        return resultMap[n]
# leetcode submit region end(Prohibit modification and deletion)
