#  in the dictionary representation of a graph :  keys are the nodes and the values of the nodes are the lists 
# of nodes that the key is connected to
class Graph: 
    def __init__(self) -> None:
        self.graph = {}

    def add_edges(self, u , v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def display_graph(self):
        print("{")
        for node, neighbors in self.graph.items():
            neighbor_str = ', '.join(map(str, neighbors))
            print(f"    {node}: [{neighbor_str}],")
        print("}")


graph = Graph()
graph.add_edges(0,1)
graph.add_edges(0,2)
graph.add_edges(1,2)
graph.add_edges(2,3)

graph.display_graph()

