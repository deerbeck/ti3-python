# define dicts using given graph
a = {"element": "A", "printed": False}
b = {"element": "B", "printed": False}
c = {"element": "C", "printed": False}
d = {"element": "D", "printed": False}

# add transitions to dicts via the "next" key
a["next"] = [b]
b["next"] = [c, d]
c["next"] = [b]
d["next"] = [a]


def printnodes(nodes, level=0):
    #print out node and 
    print(" "*level + "{}->".format(nodes["element"]))
    
    #check if node was already covered and exit function if so
    if nodes["printed"] == True:
        return
    #mark node as covered
    nodes["printed"] = True
    
    #iterated through any following nodes
    for e in nodes["next"]:
        printnodes(e, level+1)


printnodes(b)