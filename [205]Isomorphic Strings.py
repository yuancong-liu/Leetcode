# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapSToT = {}
        mapTToS = {}
        for i in range(len(s)):
            if s[i] not in mapSToT:
                mapSToT[s[i]] = t[i]
            else:
                if mapSToT[s[i]] != t[i]:
                    return False

        for i in range(len(t)):
            if t[i] not in mapTToS:
                mapTToS[t[i]] = s[i]
            else:
                if mapTToS[t[i]] != s[i]:
                    return False

        return True

# leetcode submit region end(Prohibit modification and deletion)
