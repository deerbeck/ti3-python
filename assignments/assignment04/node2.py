class Node:
    # declare id as constant variable for that node
    __id = 0

    def __init__(self, name: str) -> None:

        # hand over initialized variables
        self.__name = name
        self.next = [self]

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
            printlist = []
            #loop through __next nodes and print out working tree of nodes
            for i in range(n-2):
                printlist.append(f"{self.next[i].__name} ---> {self.next[i+1].__name}\n")
            #return last element of working tree formated like below
            printlist.append(len(self.next[-3].__name) * " " + " " + f"---> {self.next[-1].__name}")
            return "".join(printlist)



if __name__ == "__main__":
    # testing area
    n1 = Node('A')
    print(n1.name)
    n1.name = 'B'      # die Zeile soll zu einem Fehler führen!
    pass
