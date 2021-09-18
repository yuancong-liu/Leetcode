# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        tmp = ""
        length = 0
        maximum = length
        n = len(s)
        for i in range(n):
            if s[i] not in tmp:
                tmp += s[i]
                length += 1
            else:
                tmp = tmp[tmp.index(s[i]) + 1:]
                tmp += s[i]
                length = len(tmp)
            maximum = max(maximum, length)
        return maximum
# leetcode submit region end(Prohibit modification and deletion)
