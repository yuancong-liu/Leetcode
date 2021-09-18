# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        fibonacci = [0, 1]
        for i in range(2, n + 1):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci[n]
# leetcode submit region end(Prohibit modification and deletion)
