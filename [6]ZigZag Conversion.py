# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [[] for _ in range(numRows)]
        if numRows == 1:
            return s
        elif numRows == 2:
            for position in range(len(s)):
                if position % 2 == 0:
                    zigzag[0].append(s[position])
                else:
                    zigzag[1].append(s[position])
        else:
            current = 0
            flag = 0  # reverse or not
            for position in range(len(s)):
                if current < numRows:
                    zigzag[current].append(s[position])
                    if flag:
                        current -= 1
                    else:
                        current += 1
                if current == 0:
                    flag = 0
                elif current == numRows:
                    current -= 2
                    flag = 1
        return "".join([item for sublist in zigzag for item in sublist])
# leetcode submit region end(Prohibit modification and deletion)
