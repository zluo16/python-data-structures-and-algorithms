# Edge list
edges = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent list
adj = {
    0: [2],
    1: [2, 3],
    2: [0, 1, 3],
    3: [1, 2],
}

# Adjacency matrix
adj_m = {
    0: [0, 0, 1, 0],
    1: [0, 0, 1, 1],
    2: [1, 1, 0, 1],
    3: [0, 1, 1, 0],
}


class Graph:

    def __init__(self):
        self.numberofnodes = 0
        self.adjacentlist = {}

    def __str__(self):
        return str(self.__dict__)

    def add_vertex(self, node):
        if node in self.adjacentlist:
            return None
        self.adjacentlist[node] = []
        self.numberofnodes += 1
        return self.adjacentlist

    def add_edge(self, node1, node2):
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)
        return self.adjacentlist

    def show_connection(self):
        for vertex, neighbors in self.adjacentlist.items():
            print(vertex, end='-->')
            print(' '.join(neighbors))


myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4')
myGraph.add_edge('4', '2')
myGraph.add_edge('4', '5')
myGraph.add_edge('1', '2')
myGraph.add_edge('1', '0')
myGraph.add_edge('0', '2')
myGraph.add_edge('6', '5')
print(myGraph)
myGraph.show_connection()

