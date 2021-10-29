# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        words = s.split()

        return len(words[-1])
        
# leetcode submit region end(Prohibit modification and deletion)
