# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 1
        while n ** 2 <= x:
            n += 1
        return n-1
        
# leetcode submit region end(Prohibit modification and deletion)
