# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        countMap = {}
        for char in s:
            if char not in countMap:
                countMap[char] = s.count(char)

        flag = 0
        length = 0
        for item in countMap.values():
            if item % 2 == 0:
                length += item
            if item % 2 != 0:
                length += item - 1
                flag = 1

        length += flag
        return length
# leetcode submit region end(Prohibit modification and deletion)
