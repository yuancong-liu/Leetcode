# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            if not t:
                return False
            if char in t:
                t = t[t.index(char) + 1:]
            else:
                return False

        return True
# leetcode submit region end(Prohibit modification and deletion)
