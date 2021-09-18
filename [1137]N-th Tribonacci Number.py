# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci = [0, 1, 1]
        for i in range(3, n + 1):
            tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3])

        return tribonacci[n]
# leetcode submit region end(Prohibit modification and deletion)
