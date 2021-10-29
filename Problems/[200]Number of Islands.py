# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(i, j, r, c, grid)

        return count

    def dfs(self, i, j, r, c, grid):
        if 0 <= i < r and 0 <= j < c and grid[i][j] == "1":
            grid[i][j] = "2"
            if i - 1 >= 0:
                self.dfs(i - 1, j, r, c, grid)
            if i + 1 <= r:
                self.dfs(i + 1, j, r, c, grid)
            if j - 1 >= 0:
                self.dfs(i, j - 1, r, c, grid)
            if j + 1 <= c:
                self.dfs(i, j + 1, r, c, grid)
        else:
            return
# leetcode submit region end(Prohibit modification and deletion)
