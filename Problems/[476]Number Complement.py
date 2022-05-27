# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(list(map(lambda x: '1' if x == '0' else '0', bin(num)[2:]))), 2)
        
# leetcode submit region end(Prohibit modification and deletion)
