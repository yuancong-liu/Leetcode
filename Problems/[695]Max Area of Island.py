# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        print(r, c)
        count = 0
        lengths = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    count += 1
                    length = 0
                    length = self.dfs(i, j, r, c, grid, length)
                    lengths.append(length)
        if count == 0:
            return 0
        return max(lengths)

    def dfs(self, i, j, r, c, grid, length):
        if 0 <= i < r and 0 <= j < c and grid[i][j] == 1:
            grid[i][j] = 2
            length += 1
            if i - 1 >= 0:
                length = self.dfs(i - 1, j, r, c, grid, length)
            if i + 1 <= r:
                length = self.dfs(i + 1, j, r, c, grid, length)
            if j - 1 >= 0:
                length = self.dfs(i, j - 1, r, c, grid, length)
            if j + 1 <= c:
                length = self.dfs(i, j + 1, r, c, grid, length)
            return length
        else:
            return length
# leetcode submit region end(Prohibit modification and deletion)
