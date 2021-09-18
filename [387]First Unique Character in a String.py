# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequencies = {}
        for char in s:
            if char not in frequencies.keys():
                frequencies[char] = s.count(char)

        for item in frequencies.items():
            if item[1] == 1:
                return s.index(item[0])
        return -1
# leetcode submit region end(Prohibit modification and deletion)
