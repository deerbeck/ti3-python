import pytest

import glob
from radon.raw import analyze
import sys, os
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def get_commit_count_exclude_user(folder_path, username):

    cmd = ["git", "log", "--format='%H %an'", "--", folder_path]
    
    output = subprocess.check_output(cmd).decode('utf-8')
    commits = output.split('\n')
    flohr_commits = [username in el for el in commits]
    return len(commits) - sum(flohr_commits) -1


def test_codequality():
    ncomments = 0
    nloc = 0
    files_grabbed = glob.glob("./node*") + glob.glob("./edge.py") + glob.glob("./graph.py")
    for filename in files_grabbed:
        with open(filename) as fobj:
            source = fobj.read()
            report =  analyze(source)
            ncomments+=report.comments
            nloc+=report.loc
    assert nloc != 0
    print("#comments:",ncomments,"#loc:",nloc, "#comments/#loc:", ncomments / nloc)
    assert ncomments / nloc >= 0.25


def test_commit_messages():
    count = get_commit_count_exclude_user("./", "Fabian Flohr")
    assert int(count)>=5

def testTask11():
    import node1
    print("Test zu Aufgabe 1.1")
    n1 = node1.Node('A')
    n2 = node1.Node('B')
    n3 = node1.Node('C')
    n1.next.append(n2)
    n1.next.append(n3)
    assert str(n3.name) == "C"
    assert str(n1) == "A ---> B\n  ---> C"
    assert str(n2) == "B <end>"

def testTask12():
    import node2
    print("Test zu Aufgabe 1.2")
    n1 = node2.Node('A')
    n2 = node2.Node('B')
    n3 = node2.Node('C')
    n1.next.append(n2)
    n1.next.append(n3)
    assert str(n3.name) == "C"
    assert str(n1) == "A ---> B\n  ---> C"
    assert str(n2) == "B <end>"
    n4 = node2.Node('D')
    assert n4.name == "D"

def testTask13_15():
    import node3
    print("Test zu Aufgabe 1.3 bis 1.5")
    n1 = node3.Node()
    n2 = node3.Node('B')
    n3 = node3.Node()
    n1.connect(n2)
    n1.connect(n3)
    assert str(n1) == "Knoten 1 ---> B\n         ---> Knoten 3"
    assert str(n2) == "B <end>"
    t = n1.get_connects()
    assert t == (n2, n3)

def testTask21():
    import node3
    import edge
    print("Test zu Aufgabe 2.1")
    n1 = node3.Node('A')
    e1 = edge.Edge('E', 5)
    e1.connect(n1)
    assert str(e1) == "E/5"
    e1.weight = 3
    assert str(e1) == "E/3"

def testTask22():
    import node
    import edge
    print("Test zu Aufgabe 2.2")
    n1 = node.Node('A')
    n2 = node.Node('B')
    n3 = node.Node('C')
    e1 = edge.Edge('E', 5)
    e2 = edge.Edge('F', 2)
    n1.connect(e1)
    n1.connect(e2)
    e1.connect(n2)
    e2.connect(n3)
    assert str(n1) == "A --E/5--> B\n  --F/2--> C"
    assert str(n2) == "B <end>"

def testTask31_32():
    import node
    import edge
    import graph
    print("Test zu Aufgabe 3.1 bis 3.2")
    node.Node._Node__id = 0
    g = graph.Graph()
    n1 = g.new_node('A')
    n2 = g.new_node()
    e1 = g.new_edge('E', 5)
    n1.connect(e1)
    e1.connect(n2)
    ea = g.new_edge("a", 1)
    eb = g.new_edge("b", 2)
    ec = g.new_edge("c", 3)
    assert str(g) == "Knoten:\n-------\nA --E/5--> Knoten 2\n" \
                     + "Knoten 2 <end>\n\nKanten:\n-------\nE/5\n" \
                     + "a/1\nb/2\nc/3\n"
    n2_new = g.find_node("Knoten 2")
    assert isinstance(n2_new, node.Node)
    assert str(n2_new) == "Knoten 2 <end>"
    eb_new = g.find_edge("b")
    assert isinstance(eb_new, edge.Edge)
    assert str(eb_new) == "b/2"
    print(e1)

def testTask33():
    print("Test zu Aufgabe 3.3")
    import node
    import graph
    node.Node._Node__id = 0
    g = graph.Graph()
    A = g.new_node('A')
    B = g.new_node('B')
    C = g.new_node('C')
    D = g.new_node('D')
    E = g.new_node('E')
    F = g.new_node('F')
    a = g.new_edge('a', 3)
    a.connect(B)
    b = g.new_edge('b', 7)
    b.connect(C)
    c = g.new_edge('c', 5)
    c.connect(D)
    d = g.new_edge('d', 4)
    d.connect(E)
    e = g.new_edge('e', 2)
    e.connect(A)
    f = g.new_edge('f', 1)
    f.connect(B)
    A.connect(a)
    B.connect(b)
    C.connect(c)
    C.connect(d)
    D.connect(e)
    F.connect(f)
    assert g.path_length(["A", "B", "C", "D", "A"]) == 17
    assert g.path_length(["A", "B", "C", "A"]) == -1
    assert g.path_length(["A", "B", "C", "E"]) == 14

def testTask41_42():
    import reader
    print("Test zu Aufgabe 4.1 bis 4.2")
    r1 = reader.Reader()
    g1 = r1.read("Karte.xml")
    s = str(g1)
    assert "inzerer" in s
    assert "rresstr" in s
    assert "othstr" in s
    assert "chelling" in s
    assert "ranach" in s
    assert "eor" in s


if __name__ == "__main__":
    test_codequality()
    test_commit_messages()
    testTask11()
    testTask12()
    testTask13_15()
    testTask21()
    testTask22()
    testTask31_32()
    testTask33()
    testTask41_42()
