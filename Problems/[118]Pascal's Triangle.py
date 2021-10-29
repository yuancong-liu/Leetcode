# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        def addLevel(level):
            nonlocal result
            nonlocal numRows

            numOfLevel = len(level)

            if numOfLevel == numRows:
                return

            if numOfLevel == 1:
                newLevel = [1, 1]
                result.append(newLevel)

            else:
                newLevel = [1]
                # add new element
                for i in range(len(level) - 1):
                    newLevel.append(level[i] + level[i + 1])
                #
                newLevel.append(1)

                result.append(newLevel)

            addLevel(newLevel)

        addLevel(result[0])

        return result
# leetcode submit region end(Prohibit modification and deletion)
