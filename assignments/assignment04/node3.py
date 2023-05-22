class Node:
    # declare id as constant variable for that node
    __id = 1

    def __init__(self, name = "Knoten " + str(__id)) -> None:

        # hand over initialized variables
        self.__name = name
        self.next = [self]

        #increment id
        Node.__id += 1

    #getter method for name
    @property
    def name(self):
        return self.__name


    def __str__(self) -> str:
        # print out working Tree of node
        if (n := len(self.next)) == 1:
            #print out end of working tree when no follow up nodes exist
            return f"{self.__name} <end>"
        else:
            #loop through next nodes and print out working tree of nodes
            for i in range(n-2):
                print(f"{self.next[i].__name} ---> {self.next[i+1].__name}")
            #return last element of working tree formated like below
            return len(self.next[-3].__name) * " " + " " + f"---> {self.next[-1].__name}"


if __name__ == "__main__":
    # testing area
    n1 = Node('A')
    n2 = Node()
    n3 = Node('C')
    n1.next.append(n2)
    n1.next.append(n3)
    print(n3.name)
    print(n1)
    print(n2)


