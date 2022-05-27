# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        currentGreedyIndex, currentSizeIndex = 0, 0
        children = 0
        while currentGreedyIndex < len(g) and currentSizeIndex < len(s):
            if g[currentGreedyIndex] <= s[currentSizeIndex]:
                children += 1
                currentGreedyIndex += 1
                currentSizeIndex += 1
            else:
                currentSizeIndex += 1
        return children
# leetcode submit region end(Prohibit modification and deletion)
