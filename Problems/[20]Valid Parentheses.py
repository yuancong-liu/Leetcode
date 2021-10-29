# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        s = list(s)
        olen = len(s)
        while len(s) != 0:
            i = 0
            while i < len(s) - 1 and len(s) != 0:
                if (s[i] == '(' and s[i + 1] == ')') or (s[i] == '[' and s[i + 1] == ']') or (
                        s[i] == '{' and s[i + 1] == '}'):
                    s.pop(i)
                    s.pop(i)
                    i = 0
                i += 1
            count += 1
            if count > olen:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
