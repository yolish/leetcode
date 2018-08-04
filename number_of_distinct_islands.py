#https://leetcode.com/problems/number-of-distinct-islands/description/ 
class Solution(object):
    def follow_trail(self, grid, trail, m, n, i, j, visited, land):
        grid[i][j] = visited
        if i > 0 and grid[i - 1][j] == land:
            trail.append("top")
            self.follow_trail(grid, trail, m, n, i - 1, j, visited, land)
        else:
            trail.append("x")
        if j > 0 and grid[i][j - 1] == land:
            trail.append("left")
            self.follow_trail(grid, trail, m, n, i, j - 1, visited, land)
        else:
            trail.append("x")
        if i < m - 1 and grid[i + 1][j] == land:
            trail.append("bottom")
            self.follow_trail(grid, trail, m, n, i + 1, j, visited, land)
        else:
            trail.append("x")
        if j < n - 1 and grid[i][j + 1] == land:
            trail.append("right")
            self.follow_trail(grid, trail, m, n, i, j + 1, visited, land)
        else:
            trail.append("x")

    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        a translated island will have the same follow-trail route
        [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

        [[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]]
        110
        011
        000
        111
        010

        '''
        land = 1
        visited = 2

        trails = set()
        m = len(grid)
        if m > 0:
            n = len(grid[0])
            for i in xrange(m):
                for j in xrange(n):
                    if grid[i][j] == land:
                        my_trail = []
                        self.follow_trail(grid, my_trail, m, n, i, j, visited, land)
                        my_trail = ",".join(my_trail)
                        print my_trail
                        if my_trail not in trails:
                            trails.add(my_trail)
        return len(trails)

