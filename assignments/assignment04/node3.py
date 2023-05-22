class Node:
    # declare id as constant variable for that node
    __id = 0

    def __init__(self, name = None) -> None:
        
        #increment id
        Node.__id += 1

        # hand over initialized variables and set name depending on input
        if name is None:
            self.__name= "Knoten " + str(self.__id)
        else:
            self.__name = name

        self.__next = [self]

    #getter method for name
    @property
    def name(self):
        return self.__name
    
    #add nodes with this connect method
    def connect(self, node):
        self.__next.append(node)

    #getter method for nodes
    def get_connects(self):
        return tuple(self.__next[1:])


    def __str__(self) -> str:
        # print out working Tree of node
        if (n := len(self.__next)) == 1:
            #print out end of working tree when no follow up nodes exist
            return f"{self.__name} <end>"
        else:
            printlist = []
            #loop through __next nodes and print out working tree of nodes
            for i in range(n-2):
                printlist.append(f"{self.__next[i].__name} ---> {self.__next[i+1].__name}\n")
            #return last element of working tree formated like below
            printlist.append(len(self.__next[-3].__name) * " " + " " + f"---> {self.__next[-1].__name}")
            return "".join(printlist)


if __name__ == "__main__":
    n1 = Node()
    n2 = Node('B')
    n3 = Node()
    n1.connect(n2)
    n1.connect(n3)
    print(n1)
    print(n2)

