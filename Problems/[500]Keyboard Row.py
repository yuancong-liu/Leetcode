# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        rows = [set(item) for item in rows]

        wordLetterMap = {}
        for word in words:
            wordLetterMap[word] = set(word.lower())

        ans = []
        for word in words:
            for row in rows:
                if wordLetterMap[word].issubset(row):
                    ans.append(word)

        return ans
# leetcode submit region end(Prohibit modification and deletion)
