# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        magazine = list(magazine)
        for letter in ransomNote:
            if letter not in magazine:
                return False
            else:
                magazine.pop(magazine.index(letter))
        return True
# leetcode submit region end(Prohibit modification and deletion)
