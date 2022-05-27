# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x)[2:]
        b = bin(y)[2:]
        if len(a) > len(b):
            a, b = b, a

        a = "0" * (len(b) - len(a)) + a
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1

        return diff
# leetcode submit region end(Prohibit modification and deletion)
