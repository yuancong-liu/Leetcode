# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBits(self, n: int) -> List[int]:
        threshold = 1
        dynamicPro = [0] * (n + 1)
        for i in range(1, n + 1):
            if i == threshold * 2:
                threshold *= 2
            dynamicPro[i] = dynamicPro[i % threshold] + 1

        return dynamicPro

# leetcode submit region end(Prohibit modification and deletion)
