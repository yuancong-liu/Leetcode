# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = Counter([char for char in licensePlate.lower() if "a" <= char <= "z"])
        result = ""
        chars = set(licensePlate.keys())
        minLength = 1001

        for word in words:
            tmp = Counter(word)
            length = len(word)
            if not chars.issubset(set(word)):
                continue
            flag = 1
            for char in list(chars):
                if tmp[char] < licensePlate[char]:
                    flag = 0
                    break
            if flag == 1:
                if length < minLength:
                    result = word
                    minLength = length

        return result

# leetcode submit region end(Prohibit modification and deletion)
