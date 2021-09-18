# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        processed = {}
        while True:
            if n in processed:
                return False
            sumUp = 0
            for num in list(str(n)):
                sumUp += int(num) ** 2
            if sumUp == 1:
                return True
            processed[n] = sumUp
            n = sumUp

# leetcode submit region end(Prohibit modification and deletion)
