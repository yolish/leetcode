class Solution(object):
    def follow_trail(self, grid, m, n, i, j, visited, land):
        grid[i][j] = visited
        if i > 0 and grid[i - 1][j] == land:
            self.follow_trail(grid, m, n, i - 1, j, visited, land)
        if j > 0 and grid[i][j - 1] == land:
            self.follow_trail(grid, m, n, i, j - 1, visited, land)
        if i < m - 1 and grid[i + 1][j] == land:
            self.follow_trail(grid, m, n, i + 1, j, visited, land)
        if j < n - 1 and grid[i][j + 1] == land:
            self.follow_trail(grid, m, n, i, j + 1, visited, land)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        observation: we can traverse the matrix row by row , if we can connect grid[i,j] to another piece of land vertically or horizontally then it's the same island, otherwise, we are on the look for a new island .
        """
        '''
        [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
        x1000
        11000
        00100
        11000

        11000
        11000
        00100
        00011


        [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
        11110
        11010
        11000
        00000


        xx000
        xx000
        00x00
        000xx

        [["1","1","1"],["0","1","0"],["1","1","1"]]

        xxx
        0x0
        xxx


        [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
        x0xxx
        x0x0x
        xxx0x


        [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
        [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
        [["1","1","1"],["0","1","0"],["1","1","1"]]


        '''
        n_islands = 0
        land = "1"
        visited = "x"
        m = len(grid)
        if m > 0:
            n = len(grid[0])
            for i in xrange(m):
                for j in xrange(n):
                    if grid[i][j] == land:
                        # follow the trail
                        self.follow_trail(grid, m, n, i, j, visited, land)
                        n_islands = n_islands + 1

        return n_islands