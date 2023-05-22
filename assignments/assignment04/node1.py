class Node:
    # declare id as constant variable for that node
    __id = 0

    def __init__(self, name: str) -> None:

        # hand over initialized variables
        self.name = name
        self.next = [self]

    def __str__(self) -> str:
        # print out working Tree of node
        if (n := len(self.next)) == 1:
            #print out end of working tree when no follow up nodes exist
            return f"{self.name} <end>"
        else:
            printlist = []
            #loop through __next nodes and print out working tree of nodes
            for i in range(n-2):
                printlist.append(f"{self.next[i].name} ---> {self.next[i+1].name}\n")
            #return last element of working tree formated like below
            printlist.append(len(self.next[-3].name) * " " + " " + f"---> {self.next[-1].name}")
            return "".join(printlist)


if __name__ == "__main__":
    # testing area
    # n1 = Node('A')
    # n2 = Node('B')
    # n3 = Node('C')
    # n1.next.append(n2)
    # n1.next.append(n3)
    # print(n3.name)
    # print(n1)
    # print(n2)
    pass