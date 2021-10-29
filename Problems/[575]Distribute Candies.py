# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyTypeSet = set(candyType)
        if len(candyTypeSet) > len(candyType)/2:
            return int(len(candyType)/2)
        else:
            return len(candyTypeSet)
# leetcode submit region end(Prohibit modification and deletion)
