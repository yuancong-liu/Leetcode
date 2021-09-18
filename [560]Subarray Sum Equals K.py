# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        map = {0: 1}
        count = 0
        for num in nums:
            prefix += num
            if prefix - k in map:
                count += map[prefix - k]
            map[prefix] = map.get(prefix, 0) + 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
