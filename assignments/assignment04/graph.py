import node
import edge

class Graph:

    def __init__(self) -> None:
        #initialize empty nodes and edges lists
        self.__nodes = []
        self.__edges = []
    
    def new_node(self, name = None) -> node.Node:
        #add new node object with given name to node list
        self.__nodes.append(n := node.Node(name))
        return n
    
    def new_edge(self, name = None, weight = 0) -> edge.Edge:
        #add new edge object with given name to edge list
        self.__edges.append(e := edge.Edge(name, weight))
        return e
    
    def find_node(self, name) -> node.Node:
        ##loop through all nodes and return node when found else None
        for n in self.__nodes:
            if n.name == name:
                return n
        
        return None

    def find_edge(self, name) -> edge.Edge:
        ##loop through all edges and return edge when found else None
        for e in self.__edges:
            if e.name == name:
                return e
        
        return None


    def __str__(self) -> str:
        ##prefill printlist with nodes decsription
        printlist = ["Knoten:\n-------\n"]

        #loop through nodes and its connections
        for nodes in (self.__nodes):
            printlist.append(f"{nodes}")
        
        #fill printlist with edges
        printlist.append("\n\nKanten:\n-------\n")

        #loop through edges and its connections
        for edges in self.__edges:
            printlist.append(f"{edges}")
        
        #return joint printlist
        return "".join(printlist)
                             
                          
        



if __name__ == "__main__":
    g = Graph()
    n1 = g.new_node('A')
    n2 = g.new_node()
    e1 = g.new_edge('E', 5)
    n1.connect(e1)
    e1.connect(n2)
    print(g)
    pass