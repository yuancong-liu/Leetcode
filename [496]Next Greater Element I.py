# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2MonoStack = defaultdict(lambda: -1)
        monoStack = []
        for num in nums2:
            while monoStack and num > monoStack[-1]:
                num2MonoStack[monoStack.pop()] = num
            monoStack.append(num)

        return [num2MonoStack[i] for i in nums1]

# leetcode submit region end(Prohibit modification and deletion)
