# leetcode submit region begin(Prohibit modification and deletion)
import re

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if re.fullmatch('^10{0,}$', bin(n)[2:]) is None:
            return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
