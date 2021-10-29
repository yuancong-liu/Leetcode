# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        for digit in digits:
            num += str(digit)
        num = str(int(num) + 1)

        return list(num)

# leetcode submit region end(Prohibit modification and deletion)
