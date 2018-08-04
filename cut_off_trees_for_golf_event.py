class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.nbrs = set()
        self.dist = 0
        self.visited = False


class Graph(object):
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        v = self.vertices.get(key)
        if v is None:
            v = Vertex(key)
            self.vertices[key] = v
        return v

    def add_edge(self, k1, k2):
        v1 = self.add_vertex(k1)
        v2 = self.add_vertex(k2)
        v1.nbrs.add(v2)
        v2.nbrs.add(v1)


class Solution(object):
    def bfs(self, g, s, t):
        distance = -1
        queue = [g.vertices.get(s)]
        reached_t = False
        modified_vertices = set()
        while len(queue) > 0 and not reached_t:
            curr = queue.pop(0)
            nbrs = curr.nbrs
            for v in nbrs:
                if not v.visited:
                    modified_vertices.add(v)
                    v.visited = True
                    v.dist = curr.dist + 1
                    queue.append(v)
                if v.key == t:
                    reached_t = True
                    distance = v.dist
                    break
        for v in modified_vertices:
            v.dist = 0
            v.visited = False

        return distance

    def get_val(self, val, i, j, m, n):
        if val != 1:
            return val
        else:
            return -1 * (i * m + j + 1)

    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        '''
        need to know the next minimum 
        create a graph and do bfs from current to next minimum until we're done.
        each vertex will hold its height (this will be its key). 
        note: we can only go up/down/left/right
        '''

        trees = []
        g = Graph()
        m = len(forest)
        start_val = 0
        if m > 0:
            n = len(forest[0])
            for i in xrange(m):
                for j in xrange(n):
                    my_val = self.get_val(forest[i][j], i, j, m, n)
                    if i == 0 and j == 0:
                        if my_val == 0:
                            return -1
                        else:
                            start_val = my_val
                    if my_val != 0:
                        if my_val > 0:
                            trees.append(my_val)
                        g.add_vertex(my_val)
                        # consider all potential neighbors and add
                        nbrs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                        for (u, v) in nbrs:
                            if v >= 0 and v < n and u >= 0 and u < m:
                                other_val = self.get_val(forest[u][v], u, v, m, n)
                                if other_val != 0:
                                    g.add_edge(my_val, other_val)

        n_steps = -1
        if len(trees) > 0 and len(g.vertices.get(start_val).nbrs) > 0:
            n_steps = 0
            trees.sort()
            next_index = 0
            if trees[0] == start_val:
                next_index = 1
            k = len(trees)
            while next_index < k:
                curr_n_steps = self.bfs(g, start_val, trees[next_index])
                if curr_n_steps == -1:
                    n_steps = -1
                    break
                else:
                    n_steps = n_steps + curr_n_steps
                    start_val = trees[next_index]
                    next_index = next_index + 1

        return n_steps








