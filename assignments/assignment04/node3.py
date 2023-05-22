class Node:
    # declare id as constant variable for that node
    __id = 0

    def __init__(self, name = None) -> None:
        
        #increment id
        Node.__id += 1

        # hand over initialized variables
        if name is None:
            self.__name= "Knoten " + str(self.__id)
        else:
            self.__name = name

        self.__next = [self]



    
    #getter method for name
    @property
    def name(self):
        return self.__name
    
    #connect nodes through connect method
    def connect(self, node):
        self.__next.append(node)


    def __str__(self) -> str:
        # print out working Tree of node
        if (n := len(self.__next)) == 1:
            #print out end of working tree when no follow up nodes exist
            return f"{self.__name} <end>"
        else:
            #loop through __next nodes and print out working tree of nodes
            for i in range(n-2):
                print(f"{self.__next[i].__name} ---> {self.__next[i+1].__name}")
            #return last element of working tree formated like below
            return len(self.__next[-3].__name) * " " + " " + f"---> {self.__next[-1].__name}"


if __name__ == "__main__":
    n1 = Node()
    n2 = Node('B')
    n3 = Node()
    n1.connect(n2)
    n1.connect(n3)
    print(n1)
    print(n2)

