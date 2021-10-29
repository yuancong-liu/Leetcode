# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sMap = {}
        tMap = {}

        for char in s:
            if char not in sMap:
                sMap[char] = s.count(char)

        for char in t:
            if char not in tMap:
                tMap[char] = t.count(char)

        for key in tMap.keys():
            if key not in sMap or tMap[key] != sMap[key]:
                return key
# leetcode submit region end(Prohibit modification and deletion)
