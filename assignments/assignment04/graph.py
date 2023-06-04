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


    @staticmethod
    def find_edge_between(n1,n2):

        ##loop through all edges in n1 and look for a connection to n2 
        for e in n1.get_connects():
            if e.get_connect() == n2:
                #if connection to n2 is found return connecting edge
                return e
        ##loop through all edges in n2 and look for a connection to n1
        for e in n2.get_connects():
            if e.get_connect() == n1:
                #if connection to n1 is found return connecting edge
                return e
        #if no connection is found return None
        return None

    
    def path_length(self, path_node_names):
        #initialize pathlength to 0
        pathlength = 0
        
        #loop through given path node names
        for i in range(len(path_node_names)-1):
            #use static helper function to find edge inbetween
            n1 = self.find_node(path_node_names[i])
            n2 = self.find_node(path_node_names[i+1])
            e = self.find_edge_between(n1,n2)
            
            #check for found edge between nodes and add to pathlength if so
            if e is None:
                return -1
            else:
                pathlength += e.weight
        return pathlength


    def __str__(self) -> str:
        ##prefill printlist with nodes decsription
        printlist = ["Knoten:\n-------\n"]

        #loop through nodes and its connections
        for nodes in (self.__nodes):
            printlist.append(f"{nodes}\n")
        
        #fill printlist with edges
        printlist.append("\nKanten:\n-------\n")

        #loop through edges and its connections
        for edges in self.__edges:
            printlist.append(f"{edges}\n")
        
        #return joint printlist
        return "".join(printlist)
                             
                          
        



if __name__ == "__main__":
    # g = Graph()
    # n1 = g.new_node('A')
    # n2 = g.new_node('B')
    # n3 = g.new_node('C')
    # n4 = g.new_node('D')
    # n5 = g.new_node('E')
    # e1 = g.new_edge('E', 5)
    # e2 = g.new_edge('F', 8)
    # e3 = g.new_edge('G', 2)
    # e4 = g.new_edge('H', 6)
    
    # n1.connect(e1)
    # n2.connect(e2)
    # n3.connect(e3)
    # n4.connect(e4)

    # e1.connect(n2)
    # e2.connect(n3)
    # e3.connect(n4)
    # e4.connect(n5)
    # print(g)
    # print(g.path_length(["A","B","B","E"]))
    pass