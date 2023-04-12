import ass02 as p02
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
    for filename in glob.glob("./ass02*"):
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

def testAufgabe1():
    print("\nTest zu Aufgabe 1")
    area = p02.create_area((1, 5))
    assert area is None
    area = p02.create_area((5, 1))
    assert area is None
    area = p02.create_area((11, 2))
    assert area is None
    area = p02.create_area((2, 11))
    assert area is None
    m = 6
    n = 8
    area = p02.create_area((m, n))
    assert area is not None
    assert isinstance(area, list)
    assert len(area) == m
    assert len(area[0]) == n
    assert id(area[0] != id(area[1]))


def testAufgabe2():
    print("\nTest zu Aufgabe 2")
    m = 7
    n = 8
    area = p02.create_area((m, n))
    p02.fill_area(area, (1, 2), True, 5)
    assert all([e == 'X' for e in area[1][2:7]]) == True
    p02.fill_area(area, (3, 4), False, 3)
    assert all([area[2][4] == ' ',
                area[3][4] == 'X',
                area[4][4] == 'X',
                area[5][4] == 'X',
                area[6][4] == ' ']) == True

def testAufgabe4():
    print("\nTest zu Aufgabe 4")
    m = 7
    n = 8
    area = p02.create_area((m, n))
    p02.fill_area(area, (1, 2), True, 5)
    p02.fill_area(area, (3, 4), False, 3)

    #  Horizontal
    assert p02.check_area(area, (-1, 2), True, 4) == False
    assert p02.check_area(area, (2, 8), True, 4) == False
    assert p02.check_area(area, (2, -1), True, 4) == False
    assert p02.check_area(area, (2, 5), True, 4) == False
    assert p02.check_area(area, (3, 3), True, 3) == False
    assert p02.check_area(area, (5, 3), True, 3) == False
    assert p02.check_area(area, (1, 0), True, 3) == False

    assert p02.check_area(area, (1, 0), True, 2) == True
    assert p02.check_area(area, (0, 0), True, 8) == True
    assert p02.check_area(area, (2, 0), True, 8) == True
    assert p02.check_area(area, (6, 0), True, 8) == True
    assert p02.check_area(area, (3, 5), True, 3) == True
    assert p02.check_area(area, (4, 0), True, 4) == True
    assert p02.check_area(area, (5, 5), True, 3) == True

    # Vertikal
    assert p02.check_area(area, (-1, 2), False, 4) == False
    assert p02.check_area(area, (0, 4), False, 4) == False
    assert p02.check_area(area, (0, -1), False, 4) == False
    assert p02.check_area(area, (0, 8), False, 4) == False
    assert p02.check_area(area, (0, 2), False, 3) == False
    assert p02.check_area(area, (0, 6), False, 3) == False
    assert p02.check_area(area, (5, 4), False, 2) == False

    assert p02.check_area(area, (0, 0), False, 7) == True
    assert p02.check_area(area, (0, 1), False, 7) == True
    assert p02.check_area(area, (0, 7), False, 7) == True
    assert p02.check_area(area, (2, 2), False, 5) == True
    assert p02.check_area(area, (2, 3), False, 5) == True
    assert p02.check_area(area, (2, 5), False, 5) == True
    assert p02.check_area(area, (2, 6), False, 5) == True

def count_X(area):
    counter = sum([l.count('X') for l in area])
    return counter

def testAufgabe5():
    print("\nTest zu Aufgabe 5")
    m = 7
    n = 8
    area = p02.create_area((m, n))
    p02.generate_boat(area, 5)
    p02.generate_boat(area, 4)
    p02.generate_boat(area, 3)
    p02.generate_boat(area, 2)
    assert count_X(area) == 14

def testAufgabe6():
    print("\nTest zu Aufgabe 6")
    m = 7
    n = 8
    area = p02.create_area((m, n))
    boat_spec = {2: 3, 3: 2,  4: 1}
    p02.generate_boat(area, boat_spec)
    assert count_X(area) == 16

if __name__ == '__main__':
    test_codequality()
    test_commit_messages()
    testAufgabe1()
    testAufgabe2()
    testAufgabe4()
    testAufgabe5()
    testAufgabe6()
