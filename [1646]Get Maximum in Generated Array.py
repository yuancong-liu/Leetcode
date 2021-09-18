# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        generated = [0 for _ in range(n + 1)]
        if n > 0:
            generated[1] = 1
        for i in range(1, n + 1):
            if generated[-1] == 0:
                if 2 * i < n + 1:
                    generated[2 * i] = generated[i]
                if 2 * i + 1 < n + 1:
                    generated[2 * i + 1] = generated[i] + generated[i + 1]
            else:
                break
        return max(generated)

# leetcode submit region end(Prohibit modification and deletion)
