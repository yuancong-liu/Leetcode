# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        needle_len = len(needle)
        if needle_len > len(haystack):
            return -1
        for i in range(len(haystack) - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i

        return -1
# leetcode submit region end(Prohibit modification and deletion)
