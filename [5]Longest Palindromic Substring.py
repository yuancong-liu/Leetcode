# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return
        n = len(s)
        longest = ""
        for i in range(n):
            oneway = 0
            if i + 1 < n and s[i] == s[i + 1]:
                while oneway + i + 1 < n and i - oneway >= 0 and s[i - oneway] == s[i + oneway + 1]:
                    if 2 * oneway + 2 > len(longest):
                        longest = s[i - oneway:i + oneway + 2]
                    oneway += 1
            oneway = 0
            while oneway + i < n and i - oneway >= 0 and s[i - oneway] == s[i + oneway]:
                if 2 * oneway + 1 > len(longest):
                    longest = s[i - oneway:i + oneway + 1]
                oneway += 1
        return longest
# leetcode submit region end(Prohibit modification and deletion)
