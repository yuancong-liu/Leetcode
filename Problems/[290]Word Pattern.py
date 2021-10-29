# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        map = {}
        for i in range(len(s)):
            if pattern[i] in map:
                if map[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in map.values():
                    return False
                map[pattern[i]] = s[i]
        return True
# leetcode submit region end(Prohibit modification and deletion)
