import edge


class Node:
    # declare id as constant variable for that node
    __id = 0

    def __init__(self, name=None) -> None:

        # increment id
        Node.__id += 1

        # hand over initialized variables and set name depending on input
        if name is None:
            self.__name = "Knoten " + str(self.__id)
        else:
            self.__name = name

        self.__next = []

    # getter method for name
    @property
    def name(self):
        return self.__name

    # add nodes with this connect method
    def connect(self, input):
        self.__next.append(input)

    # getter method for nodes

    def get_connects(self):
        return tuple(self.__next)

    def __str__(self) -> str:
        # print out working Tree of node
        if (n := len(self.__next)) == 0:
            # print out end of working tree when no follow up nodes exist
            return f"{self.__name} <end>"
        
        if n == 1:
            #in case of only 1 connection print that connection
            return self.__name +  f" --{self.__next[0]}--> {self.__next[0].get_connect().name}\n"
        
        else:
            # fill printlist with first node and its connection
            printlist = [self.__name +  f" --{self.__next[0]}--> {self.__next[0].get_connect().name}"]
            # loop through edges and its connected nodes and add them to the printlist
            for i in range(1, n):
                printlist.append("\n" + len(self.__name) * " " + f" --{self.__next[i]}--> {self.__next[i].get_connect().name}")
        
        #join all elements of printlist and return them
        return "".join(printlist)


if __name__ == "__main__":
    n1 = Node('A')
    n2 = Node()
    n3 = Node('C')
    n4 = Node('D')
    e1 = edge.Edge('E', 5)
    e2 = edge.Edge('F', 2)
    e3 = edge.Edge('G', 7)
    
    n1.connect(e1)
    n1.connect(e2)
    n1.connect(e3)

    e1.connect(n2)
    e2.connect(n3)
    e3.connect(n4)

    print(n1)
    print(n2)
    pass
