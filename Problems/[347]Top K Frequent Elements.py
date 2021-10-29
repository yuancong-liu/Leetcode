# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        checked = []
        frequencies = {}
        for num in nums:
            if num not in checked:
                frequencies[num] = nums.count(num)
                checked.append(num)

        output = []
        frequencies = sorted(frequencies.items(), key=lambda x: x[0])
        frequencies = sorted(frequencies, key=lambda x: x[1], reverse=True)

        for i in range(k):
            output.append(frequencies[i][0])

        return output
# leetcode submit region end(Prohibit modification and deletion)
