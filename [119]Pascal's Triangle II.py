# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        level = [1]

        def nextLevel():
            nonlocal level
            nonlocal rowIndex

            numOfLevel = len(level)

            if numOfLevel == rowIndex + 1:
                return

            if numOfLevel == 1:
                newlevel = [1, 1]
                level = newlevel


            else:
                newLevel = [1]
                # add new element
                for i in range(len(level) - 1):
                    newLevel.append(level[i] + level[i + 1])
                #
                newLevel.append(1)

                level = newLevel

            nextLevel()

        nextLevel()

        return level
# leetcode submit region end(Prohibit modification and deletion)
