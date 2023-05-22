class Edge:
    def __init__(self, name=None, weight = 0) -> None:

        # hand over initialized variables and set name depending on input
        if name is None:
            pass
        else:
            self.__name = name
            
        self.weight = weight

    # getter method for name
    @property
    def name(self):
        return self.__name

    # add nodes with this connect method
    def connect(self, n):
        #assign node object to next attribute
        self.__next = n

    # getter method for nodes
    def get_connect(self):
        #return connected edge
        return self.__next

    def __str__(self) -> str:
        #print name and weigth of edge
        return self.__name + "/" + str(self.weight)


if __name__ == "__main__":
    import node3
    n1 = node3.Node('A')
    e1 = Edge('E', 5)
    e1.connect(n1)
    print('vorher:', e1)
    e1.weight=3
    print('nachher:', e1)


