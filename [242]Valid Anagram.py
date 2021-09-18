# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        for char in t:
            if char not in s:
                return False
            s.pop(s.index(char))
        return True
# leetcode submit region end(Prohibit modification and deletion)
