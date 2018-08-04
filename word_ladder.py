class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.nbrs = set()
        self.color = "white"
        self.dist = 0

    def __str__(self):
        return str(self.key)


class Graph(object):
    def __init__(self):
        self.vertices = {}

    def get_vertex(self, key):
        return self.vertices.get(key)

    def add_vertex(self, key):
        vertex = self.get_vertex(key)
        if vertex is None:
            vertex = Vertex(key)
            self.vertices[key] = vertex
        return vertex

    def add_edge(self, k1, k2):
        v1 = self.add_vertex(k1)
        v2 = self.add_vertex(k2)
        v1.nbrs.add(v2)


class Solution(object):
    def put_in_bucket(self, w, buckets, wildcard):
        for i in xrange(len(w)):
            b = w[:i] + wildcard + w[i + 1:]
            nbrs = buckets.get(b)
            if nbrs is None:
                buckets[b] = [w]
            else:
                nbrs.append(w)

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # put words in buckets
        ladder_length = 0
        wildcard = '_'
        buckets = {}
        if endWord in wordList:
            self.put_in_bucket(beginWord, buckets, wildcard)
            for w in wordList:
                self.put_in_bucket(w, buckets, wildcard)
            # build the graph
            g = Graph()
            for b, words in buckets.items():
                for w1 in words:
                    for w2 in words:
                        if w1 != w2:
                            g.add_edge(w1, w2)
            # do partial bfs - until we find the end word
            start = g.get_vertex(beginWord)
            if start is not None:
                start.color = "grey"
                queue = [start]
                end = None
                while len(queue) > 0:
                    curr = queue.pop(0)
                    for v in curr.nbrs:
                        if v.color == "white":
                            v.color = "grey"
                            v.dist = curr.dist + 1
                            if v.key == endWord:
                                end = v
                                break
                            queue.append(v)
                    curr.color = "black"
                if end is not None:
                    ladder_length = end.dist + 1  # number of edges not nodes

        return ladder_length